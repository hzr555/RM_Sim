#include <ros/ros.h>
#include <opencv2/opencv.hpp>
#include <geometry_msgs/Twist.h>
#include <sensor_msgs/Image.h>
#include <image_transport/image_transport.h>
#include <cv_bridge/cv_bridge.h>

using namespace cv;
using namespace std;

ros::Publisher pub;

void callback(const sensor_msgs::ImageConstPtr &msg)
{
    int mouseX, mouseY, key_last = 0;
    
    namedWindow("Aimbot");
    imshow("Aimbot", cv_bridge::toCvShare(msg, "bgr8")->image);

    int key = waitKey(1);
    geometry_msgs::Twist move_cmd;

    if (key_last != key && key != -1)
        key_last = key;
    if (key == 119 || key_last == 119)
        move_cmd.linear.x = 0.6;
    if (key == 97 || key_last == 97)
        move_cmd.angular.z = 0.6;   
    if (key == 100 or key_last == 100)
        move_cmd.angular.z = -0.6;   
    if (key == 120 or key_last == 120)
        move_cmd.linear.x = -0.6;     

    pub.publish(move_cmd);

    if (key == 27 && 0xFF == 27)
        exit(0);
}

int main(int argc, char* argv[])
{
    ros::init(argc, argv, "control");
    ros::NodeHandle nh;
    image_transport::ImageTransport it(nh);

    pub = nh.advertise<geometry_msgs::Twist>("/cmd_vel", 1);
    image_transport::Subscriber sub = it.subscribe("/camera/image_raw", 1, callback);

	ros::Rate rate(200);
	while (ros::ok())
	{
		ros::spinOnce();
		rate.sleep();
	}

	return 0;
}
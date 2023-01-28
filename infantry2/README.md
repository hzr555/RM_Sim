# infantry2
--**具体流程如下，即可打开gazebo仿真** 

    catkin_make
    roslaunch infantry2 gazebo.launch
### 使用topic如下：
  --topic：
    
    /cmd_vel  #控制小车左右旋转移动
    /camera/image_raw  #小车摄像头的图像
    /camera/camera_info #摄像头参数
    /infantry/xiaotuoluo_position_controller/command #底盘小陀螺部分，角度控制
    /infantry/yuntai_position_controller/command   #云台俯仰角，角度控制

  --service

    #获取仿真世界中物体的旋转角以及惯性参数,通过model-name区分具体的物体
    /gazebo/model_status  
    #设置仿真世界中物体的旋转角以及惯性参数
    /gazebo/set_model_status  

### 使用Topic教程
  
  **使用/cmd_val可以参考testTF包中的控制程序，control.py**

  使用/infantry/yuntai_position_controller/command可以通过shell指令
  ```shell
  rostopic pub -1 /infantry/yuntai_position_controller/command std_msgs/Float64 "data: 0.5"
  ```
  其中 0.5 是可以更改的，如果 data 为 0 时为初始状态，此时可以通过 gazebo 的仿真效果，查看云台是否运动

### 使用rviz
  在 launch 文件中默认打开了机器人模型以及模型的TF，可以通过 add 按键增加想要可视化的部分

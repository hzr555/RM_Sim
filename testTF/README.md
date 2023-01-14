# testTF
--**具体流程如下，即可打开gazebo仿真** 

    catkin_make && source devel/setup.bash or .zsh
    roslaunch testTF test.launch 

### 文件夹内容
    |--testTF
        |--urdf
            |--gazebo
              |--"camera.xarco" #相机在gazebo中的参数,可以用来设定fov以及画面大小
            |--"*.xarco"    #一些urdf的文件,用于描述小车的固定属性,物理属性
        |--worlds
            |--"test.world"  #简单的仿真世界,放置了一个障碍物,体积为0.2*0.5*0.2
        |--scripts
            |--control.py #控制小车在仿真世界中运动
        |--launch
            |--gazebo.launch #用来启动gazebo以及将小车放入仿真世界中
            |--test.launch  #主启动文件,包含gazebo.launch
### 使用topic如下：
  --topic：
    
    /cmd_vel  #控制小车左右旋转移动
    /camera/image_raw  #小车摄像头的图像
    /camera/camera_info #摄像头参数
  --service

    #获取仿真世界中物体的旋转角以及惯性参数,通过model-name区分具体的物体
    /gazebo/model_status  
    #设置仿真世界中物体的旋转角以及惯性参数
    /gazebo/set_model_status  
    
###脚本介绍

    rosrun testTF *.py #运行控制程序
    
  -- contorl.py 

  通过W,A,D,X来控制小车的前进，左旋，右旋，后退，四个方向。通过OpenCV的waitKey实现对键盘按键的获取。按S可以终止当前状态。

  --showtf.py
  
  待完成，会将物体和小车的仿真世界坐标通过topic的方式发布出来。。

### END
#### **PS:** 记得给py文件权限，不然rosrun的时候找不到文件！！
    sudo chmod 777 *.py
  
# ***-->To Be Continued -->***
      
      


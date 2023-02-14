- [RM_Sim](#RM_Sim)
  - [infantry2](#infantry2)
  - [testTF](#testTF)


# RM_Sim
基于 ROS + Gazebo 仿真控制实现，更新都为ROS的package

其中作者使用的 ROS 版本为noetic，ubuntu20.04
## infantry2
使用 SolidWorks 将模型导出，并添加gazebo控制器
## testTF
使用网络上的小车模型，用来测试虚拟相机与RM的仿真地图
### 2.14
在冲浪发现了一个十分好用的 ROS 入门博客!包括了现在的建图以及仿真部分[点击这里](http://www.autolabor.com.cn/book/ROSTutorials/di-7-zhang-ji-qi-ren-dao-822a28-fang-771f29/72-dao-hang-shi-xian.html)
学习，里面包含了使用 gazebo 插件实现仿真，并且一步一步指导实现了地图的构建到导航的部分

已将 2D 雷达，相机都实现仿真效果，并通过 ros-gmapping 实现地图的绘制
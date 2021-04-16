PROJECT ROADMAP

1.create repository

  -project repository created 4/8/21
  
2.Explore reference repositries

   -For this project, I used the SweetSecurity respository by TravisFSmith at https://github.com/TravisFSmith/SweetSecurity.git to help guide my process and give me a solid    starting point for the project. While exploring this repository i dsicovered that it was designed to be used with Linux, which is the standard operating system that comes with a Raspberry Pi. The reposity has several folders included within in. One of the folders includes several files for both client and server operations and involves the installation and control of several tools including apache, and iptables. The client subfolder also includes python code files which control certain operations such as nmap scans, downloading log files, and pulling from programs like MalciousIP, as well including files to control the importing of the actual project files for the main code. The server subfolder contains python code files that control certain server operations like log retnetion and file management. This repository also utilizes Kibana and Elasticsearch, which are data visualization tools to help users get a graphical picture of what is actually happening within their network, as well as a log stashing program to help store and analyze log files. This repository also includes files that control other functions such as error handling, firewall updating, architecture support, and many others. Overall this repository is much more advanced then the project I intend to create but it is a good starting point and help give a better understanding of what will be needed moving forward to creat a successful project. When i attempted to run this code i was not able to run the code because I do not have the proper hardware or software to fully run the code. The code itself is very organizaed and well written, with many comments to help understand what each part of the code actually does.
  
3.Determine Project Requirements (completed 4/16/21)

  -Raspberry Pi
    -For this project I will need a raspberry pi to act as the computer that runs the software programs used to actually monitor the network. Using a Raspberry Pi instead of a laptop or desktop computer makes the project much more affordable while being able to have a standalone device for network monitoring, meaning that I dont have to take up my personal computer's system resources to conduct monitoring activities. Using a a stand alone device also enable the device to be portable and can be used on any network without having to have my personal computer. I chose a raspberry pi because it is a simple computer that has the necessary capabilities, it is affordable, and is light weight and easily portable. I will need the Raspberry Pi 4, the fourth generation model of Raspberry Pi, becase it has all the components I will need and enough memory/processing power, as well as several external device ports that will be useful when using this device.
    
  -Nagios
    -Nagios is a software program used to monitor networks that a system is connected to. For this project I have chosen to use Nagios because it is a free software that is powerful enough to perform the tasks needed for my Monitoring tool without having to overcomplicae the code. Nagios needs to be installed onto my Raspberry Pi in one of two ways, by installing a full disk NEMS(Nagios Enterprise Monitoring Server) Linux image, which is the more simple method, or by manually installing Nagios core onto my Raspberry Pi. I have decided to use the firt choice and install a NEMS Linux image onto my device, for this I will need a blank microSD card with atleast 16GB of memory, NEMS for Raspberry Pi, and a flash disk writing software.
    
  -16GB microSD card
    -I will need a blank microSD card with atleast 16GB of space to be able to install the necesary monitoring software(NEMS) and other necessary programs on the Raspberry Pi device.
    
  -NEMS for Raspberry Pi
    -I will need this Nagios software to conduct the monitoring activities that the project device is intended to be used for. Using the NEMS software suit makes the installation process much easier and comes with all the key configurations installed with the program, making the set up process much easier. NEMS has a variety of different checks that can be used when monitoring a network, and therefor I will need to configure each check individually and ensure that each check is working before configuring the next. That way I can add all the necessary monitoring checks I wish to include in the project, while ensuring that the entire system is running properly. 
 
  -Etcher flash disk writing software
    -For this prject I will need a fash disk writing software, which is just a bootable OS image from a USB drive. I have chosen Etcher because it is a free open-source software that is easy to use and simplifies the process of making a flash disk into a bottable drive. It also has several features such as validated flashing to help ensure the that the flash disk is installed and booted correctly. Etcher aslo supports multiple Operating Systems incase i wanted to use it for another device or load a different OS. 
  
  -RRDtool (Round Robin Database Tool)
    -This is a high-performance data logging and graphing tool used for time series data. It allows you to to store network data in a circular buffer based database, meaning that the system storage footprint remains constant over time. It is able to record data for networks such as bandwidth, temperature, CPU load, and many others that can be useful when monitoring a network. This tool is needed to capture the network activity that can be used with other software to create grpahical images of network performance. 
  
  -Cacti
    -Cacti is a network graphing tool used to create graphical images of network data. I will need this software to be used in conjunction with RRDtool and NEMS to create graphical representations of network performance data captured by the Raspberry Pi with NEMS and RRDtool. This will allow the device to capture data with RRDtool and NEMS and then give users an easy to view and understand image of how the network that the device is connected to is operating, providing insights into the network, even for somebody who is not technically oriented. 
   
  -Additional Nagios Plug-Ins
    Nagios provides a number of plugins that can be used to provide extensibility to the network monitoring tool. Once the system is set up I will have to do more research into the plug ins and decide if any of them are worth adding to the system.

4. Acquire Necessary Tools and software

  -Raspberry Pi 4
    -acquired 4/15/21. Raspberry Pi was recieved in mail, have not begun configuration yet.
  -NEMS
    -acquired software 4/16/21. Not installed on Raspberry pi yet
  -Etcher Flask image writer
    -acquired software 4/16/21. Not yet configured or used to create image
  -Cacti
    -acquired software 4/16/21. Not installed on Raspberry pi yet
  -RRDtool
    -acquired software 4/16/21. Not installed on Raspberry pi yet
  -16GB microSD card
    -not yet aquired
  -Additional Nagios plug-ins
    -not yet acquired
  
5. Begin Developement

6. Review and edit project

7. Test project

8. Review Additional Nagios Plug-Ins

9. Add Additional Plug-Ins

10.Review and edit project

11.Second project test

12.Make final adjustments

13.Conduct Final Test

14.Complete Project



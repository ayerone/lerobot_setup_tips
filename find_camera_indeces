## Background

Getting cameras mixed up between training and inference will sure ruin your day.

Of course, the lerobot library has a helper script for finding which cameras are attached, and taking a snapshot with each.  But to save time at teach boot when checking that the indeces are correct, this script uses a name that you've identified for each camera, and finds the index associated with that camera name.

On my system (Ubuntu)
```shell
v4l2-ctl --list-devices
```
```
Innomaker-U20CAM-720P  : Innoma (usb-0000:00:14.0-1.2):
	/dev/video2
	/dev/video3
	/dev/media1

Innomaker-U20CAM-1080p-S1: Inno (usb-0000:00:14.0-3):
	/dev/video0
	/dev/video1
	/dev/media0
```

I use the 720P camera on the wrist, and I use the 1080p camera on the side.

So my script "name_cameras.sh" contains:
```shell
python name_cameras.py --wrist-camera-name=Innomaker-U20CAM-720P --side-camera-name=Innomaker-U20CAM-1080p-S1
```
and outputs
```
export wrist_cam_index=2
export side_cam_index=0
```
Which you can run to set an environment variable for each camera. Then, in the shell scripts you use for lerobot-teleoperate, lerobot-record, etc, in robot.cameras, use these environment variables instead of hardcoding:
```
# old
--robot.cameras="{ wrist: {type: opencv, index_or_path: 0, width: 640, height: 480, fps: 30}, side: {type: opencv, index_or_path: 2, width: 640, height: 480, fps: 30}}"
```

```
# new
--robot.cameras="{ wrist: {type: opencv, index_or_path: ${wrist_cam_index}, width: 640, height: 480, fps: 30}, side: {type: opencv, index_or_path: ${side_cam_index}, width: 640, height: 480, fps: 30}}"
```


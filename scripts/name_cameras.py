import subprocess
import re
import argparse

def get_camera_indices(wrist_camera_name, side_camera_name):
    # Run the command and capture output
    result = subprocess.run(['v4l2-ctl', '--list-devices'], stdout=subprocess.PIPE, text=True)
    output = result.stdout

    # Find device blocks
    blocks = re.split(r'\n(?=\S)', output.strip())
    wrist_index = None
    side_index = None

    for block in blocks:
        lines = block.splitlines()
        if lines:
            if wrist_camera_name in lines[0]:
                # Find first /dev/video* line
                for line in lines[1:]:
                    match = re.search(r'/dev/video(\d+)', line)
                    if match:
                        wrist_index = match.group(1)
                        break
            elif side_camera_name in lines[0]:
                for line in lines[1:]:
                    match = re.search(r'/dev/video(\d+)', line)
                    if match:
                        side_index = match.group(1)
                        break

    return wrist_index, side_index

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Detect camera indices and output export commands.")
    parser.add_argument('--wrist-camera-name', required=True, help='Name string to identify the wrist camera (as appears in v4l2-ctl output)')
    parser.add_argument('--side-camera-name', required=True, help='Name string to identify the side camera (as appears in v4l2-ctl output)')
    args = parser.parse_args()

    wrist_index, side_index = get_camera_indices(args.wrist_camera_name, args.side_camera_name)
    if wrist_index is not None:
        print(f"export wrist_cam_index={wrist_index}")
    if side_index is not None:
        print(f"export side_cam_index={side_index}")

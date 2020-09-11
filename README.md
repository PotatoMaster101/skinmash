# Skin Mash
Combines multiple Minecraft skins into one single skin.

## Setup
Requires the [`opencv-python`](https://github.com/skvark/opencv-python) package to run. To setup using `pip3`:
```
$ git clone https://github.com/PotatoMaster101/skinmash
$ cd skinmash
$ pip3 install -r requirements.txt
```

## Usage
Run with python 3:
```
$ python3 skinmash.py [-h] [-o OUTPUT] [config]
```
If a config file is specified, then the script will run the lines in the config file. See [Config File Format](#config-file-format) for more information.

If no config file is provided, then the script will run in interactive mode. Interactive mode is exactly the same, but instead of reading from a file the script will read from `stdin` instead. Use the command `exit` or `quit` to exit interactive mode (which will also save the current output image). See [Example](#example) for examples.

## Config File Format
Each line of the config file will specify the part of the body and the skin image to use for that part of the body, using the syntax `<body part> <username>`. For example, by specifying `head PotatoMaster101`, the output skin will have the head portion of `PotatoMaster101`'s skin. The `<username>` part can also be a local file (if it ends with `.png`). The mostly used body parts are:
- `all` - entire skin for 64x64 skins (maps to `all32` on 32x64 skin)
- `all32` - entire skin for 32x64 skins
- `head` - head
- `hat` - hat
- `rleg` - right leg
- `body` - main body
- `rarm` - right arm
- `rleg2` - right leg jacket (not available for 32x64 skins)
- `jacket` - main body jacket (not available for 32x64 skins)
- `rarm2` - right arm jacket (not available for 32x64 skins)
- `lleg2` - left leg jacket (not available for 32x64 skins)
- `lleg` - left leg (maps to `rleg` for 32x64 skins)
- `larm` - left arm (maps to `rarm` for 32x64 skins)
- `larm2` - left arm jacket (not available for 32x64 skins)

Below is an example of a config file:
```
all PotatoMaster101
head skins/Wikbix.png
hat skins/Wikbix.png
lleg Llaqw
lleg2 Llaqw
rleg Llaqw
rleg2 Llaqw
larm skins/_QueenKathleen_.png
larm2 skins/_QueenKathleen_.png
rarm skins/_QueenKathleen_.png
rarm2 skins/_QueenKathleen_.png
```

Below are some lesser used, but more specific body parts:
- `head_top` - top of the head
- `head_bottom` - bottom of the head
- `head_right` - right of the head
- `head_front` - front of the head
- `head_left` - left of the head
- `head_back` - back of the head
- `hat_top` - top of the hat
- `hat_bottom` - bottom of the hat
- `hat_right` - right of the hat
- `hat_front` - front of the hat
- `hat_left` - left of the hat
- `hat_back` - back of the hat
- `rleg_top` - top of right leg
- `rleg_bottom` - bottom of right leg
- `body_top` - top of main body
- `body_bottom` - bottom of main body
- `rarm_top` - top of right arm
- `rarm_bottom` - bottom of right arm
- `rleg_right` - right of right leg
- `rleg_front` - front of right leg
- `rleg_left` - left of right leg
- `rleg_back` - back of right leg
- `body_right` - right of main body
- `body_front` - front of main body
- `body_back` - back of main body
- `body_left` - left of main body
- `rarm_right` - right of right arm
- `rarm_front` - front of right arm
- `rarm_left` - left of right arm
- `rarm_back` - back of right arm
- `rleg2_top` - top of right leg jacket (not available for 32x64 skins)
- `rleg2_bottom` - bottom of right let jacket (not available for 32x64 skins)
- `jacket_top` - top of main jacket (not available for 32x64 skins)
- `jacket_bottom` - bottom of main jacket (not available for 32x64 skins)
- `rarm2_top` - top of right arm jacket (not available for 32x64 skins)
- `rarm2_bottom` - bottom of right arm jacket (not available for 32x64 skins)
- `rleg2_right` - right of right leg jacket (not available for 32x64 skins)
- `rleg2_front` - front of right leg jacket (not available for 32x64 skins)
- `rleg2_left` - left of right leg jacket (not available for 32x64 skins)
- `rleg2_back` - back of right leg jacket (not available for 32x64 skins)
- `jacket_right` - right of main jacket (not available for 32x64 skins)
- `jacket_front` - front of main jacket (not available for 32x64 skins)
- `jacket_back` - back of main jacket (not available for 32x64 skins)
- `jacket_left` - left of main jacket (not available for 32x64 skins)
- `rarm2_right` - right of right arm jacket (not available for 32x64 skins)
- `rarm2_front` - front of right arm jacket (not available for 32x64 skins)
- `rarm2_left` - left of right arm jacket (not available for 32x64 skins)
- `rarm2_back` - back of right arm jacket (not available for 32x64 skins)
- `lleg2_top` - top of left leg jacket (not available for 32x64 skins)
- `lleg2_bottom` - bottom of left leg jacket (not available for 32x64 skins)
- `lleg_top` - top of left leg (maps to `rleg_top` for 32x64 skins)
- `lleg_bottom` - bottom of left leg (maps to `rleg_bottom` for 32x64 skins)
- `larm_top` - top of left arm (maps to `rarm_top` for 32x64 skins)
- `larm_bottom` - bottom of left arm (maps to `rarm_bottom` for 32x64 skins)
- `larm2_top` - top of left arm jacket (not available for 32x64 skins)
- `larm2_bottom` - bottom of left arm jacket (not available for 32x64 skins)
- `lleg2_right` - right of left leg jacket (not available for 32x64 skins)
- `lleg2_front` - front of left leg jacket (not available for 32x64 skins)
- `lleg2_left` - left of left leg jacket (not available for 32x64 skins)
- `lleg2_back` - back of left leg jacket (not available for 32x64 skins)
- `lleg_right` - right of left leg (maps to `rleg_right` for 32x64 skins)
- `lleg_front` - front of left leg (maps to `rleg_front` for 32x64 skins)
- `lleg_left` - left of left leg (maps to `rleg_left` for 32x64 skins)
- `lleg_back` - back of left leg (maps to `rleg_back` for 32x64 skins)
- `larm_right` - right of left arm (maps to `rarm_right` for 32x64 skins)
- `larm_front` - front of left arm (maps to `rarm_front` for 32x64 skins)
- `larm_left` - left of left arm (maps to `rarm_left` for 32x64 skins)
- `larm_back` - back of left arm (maps to `rarm_back` for 32x64 skins)
- `larm2_right` - right of left arm jacket (not available for 32x64 skins)
- `larm2_front` - front of left arm jacket (not available for 32x64 skins)
- `larm2_left` - left of left arm jacket (not available for 32x64 skins)
- `larm2_back` - back of left arm jacket (not available for 32x64 skins)

## Example
Example config files can be found under the `examples` directory.
```
$ python3 skinmash.py <example path>/conf.txt
```
Output file by default will be named `output.png` but can be changed using the `-o` flag.

Example for interactive usage:
```
$ python3 skinmash.py
skinmash> all PotatoMaster101
skinmash> head Destination666
skinmash> hat Destination666
skinmash> exit
```

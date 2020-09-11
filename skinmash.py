#!/usr/bin/env python3
####################################################################################################
# Combine multiple Minecraft skins into one.
#
# Usage: python3 skinmash.py [config_file] [-o output_file]
####################################################################################################

import argparse as ap
import numpy as np
import urllib.request as req
import base64
import json
import cv2
import sys

SKINS = {}
SKIN_PORTION = {    # portion: ((y, x, h, w), 64 only, [32 equiv])
    "all": ((0, 0, 64, 64), True, "all32"),
    "all32": ((0, 0, 32, 64), False),
    "head": ((0, 0, 16, 32), False),
    "hat": ((0, 32, 16, 32), False),
    "rleg": ((16, 0, 16, 16), False),
    "body": ((16, 16, 16, 24), False),
    "rarm": ((16, 40, 16, 16), False),
    "rleg2": ((32, 0, 16, 16), True, None),
    "jacket": ((32, 16, 16, 24), True, None),
    "rarm2": ((32, 40, 16, 16), True, None),
    "lleg2": ((48, 0, 16, 16), True, None),
    "lleg": ((48, 16, 16, 16), True, "rleg"),
    "larm": ((48, 32, 16, 16), True, "rarm"),
    "larm2": ((48, 48, 16, 16), True, None),
    "head_top": ((0, 8, 8, 8), False),
    "head_bottom": ((0, 16, 8, 8), False),
    "head_right": ((8, 0, 8, 8), False),
    "head_front": ((8, 8, 8, 8), False),
    "head_left": ((8, 16, 8, 8), False),
    "head_back": ((8, 24, 8, 8), False),
    "hat_top": ((0, 40, 8, 8), False),
    "hat_bottom": ((0, 48, 8, 8), False),
    "hat_right": ((8, 32, 8, 8), False),
    "hat_front": ((8, 40, 8, 8), False),
    "hat_left": ((8, 48, 8, 8), False),
    "hat_back": ((8, 56, 8, 8), False),
    "rleg_top": ((16, 4, 4, 4), False),
    "rleg_bottom": ((16, 8, 4, 4), False),
    "body_top": ((16, 20, 4, 8), False),
    "body_bottom": ((16, 28, 4, 8), False),
    "rarm_top": ((16, 44, 4, 4), False),
    "rarm_bottom": ((16, 48, 4, 4), False),
    "rleg_right": ((20, 0, 12, 4), False),
    "rleg_front": ((20, 4, 12, 4), False),
    "rleg_left": ((20, 8, 12, 4), False),
    "rleg_back": ((20, 12, 12, 4), False),
    "body_right": ((20, 16, 12, 4), False),
    "body_front": ((20, 20, 12, 8), False),
    "body_back": ((20, 28, 12, 8), False),
    "body_left": ((20, 36, 12, 4), False),
    "rarm_right": ((20, 40, 12, 4), False),
    "rarm_front": ((20, 44, 12, 4), False),
    "rarm_left": ((20, 48, 12, 4), False),
    "rarm_back": ((20, 52, 12, 4), False),
    "rleg2_top": ((32, 4, 4, 4), True, None),
    "rleg2_bottom": ((32, 8, 4, 4), True, None),
    "jacket_top": ((32, 20, 4, 8), True, None),
    "jacket_bottom": ((32, 28, 4, 8), True, None),
    "rarm2_top": ((32, 44, 4, 4), True, None),
    "rarm2_bottom": ((32, 48, 4, 4), True, None),
    "rleg2_right": ((36, 0, 12, 4), True, None),
    "rleg2_front": ((36, 4, 12, 4), True, None),
    "rleg2_left": ((36, 8, 12, 4), True, None),
    "rleg2_back": ((36, 12, 12, 4), True, None),
    "jacket_right": ((36, 16, 12, 4), True, None),
    "jacket_front": ((36, 20, 12, 8), True, None),
    "jacket_back": ((36, 28, 12, 8), True, None),
    "jacket_left": ((36, 36, 12, 4), True, None),
    "rarm2_right": ((36, 40, 12, 4), True, None),
    "rarm2_front": ((36, 44, 12, 4), True, None),
    "rarm2_left": ((36, 48, 12, 4), True, None),
    "rarm2_back": ((36, 52, 12, 4), True, None),
    "lleg2_top": ((48, 4, 4, 4), True, None),
    "lleg2_bottom": ((48, 8, 4, 4), True, None),
    "lleg_top": ((48, 20, 4, 4), True, "rleg_top"),
    "lleg_bottom": ((48, 24, 4, 4), True, "rleg_bottom"),
    "larm_top": ((48, 36, 4, 4), True, "rarm_top"),
    "larm_bottom": ((48, 40, 4, 4), True, "rarm_bottom"),
    "larm2_top": ((48, 52, 4, 4), True, None),
    "larm2_bottom": ((48, 56, 4, 4), True, None),
    "lleg2_right": ((52, 0, 12, 4), True, None),
    "lleg2_front": ((52, 4, 12, 4), True, None),
    "lleg2_left": ((52, 8, 12, 4), True, None),
    "lleg2_back": ((52, 12, 12, 4), True, None),
    "lleg_right": ((52, 16, 12, 4), True, "rleg_right"),
    "lleg_front": ((52, 20, 12, 4), True, "rleg_front"),
    "lleg_left": ((52, 24, 12, 4), True, "rleg_left"),
    "lleg_back": ((52, 28, 12, 4), True, "rleg_back"),
    "larm_right": ((52, 32, 12, 4), True, "rarm_right"),
    "larm_front": ((52, 36, 12, 4), True, "rarm_front"),
    "larm_left": ((52, 40, 12, 4), True, "rarm_left"),
    "larm_back": ((52, 44, 12, 4), True, "rarm_back"),
    "larm2_right": ((52, 48, 12, 4), True, None),
    "larm2_front": ((52, 52, 12, 4), True, None),
    "larm2_left": ((52, 56, 12, 4), True, None),
    "larm2_back": ((52, 60, 12, 4, True, None))
}

class Skin:
    """Represents a Minecraft skin.

    Attributes:
        img: The skin image.
        is32: Whether the skin image is 32x64.
    """
    def __init__(self, img):
        """Constructs a new `Skin`.

        Args:
            img: The skin image.

        Raises:
            ValueError: If the image is invalid or has invalid dimensions.
        """
        if (img.shape[1] != 64) or (img.shape[0] != 32 and img.shape[0] != 64):
            raise ValueError(f"bad skin dimensions: {img.shape[0]}x{img.shape[1]}")
        self.img = img
        self.is32 = (img.shape[0] == 32)

    def get_portion(self, pt):
        """Returns the specified portion of the skin.

        Args:
            pt: The portion to retrieve, in the form of (y, x, h, w).

        Returns:
            The skin portion retrieved.
        """
        y, x, h, w = pt
        return self.img[y:y + h, x:x + w]

def get_args():
    """Returns the user arguments.

    Returns:
        User arguments provided.
    """
    ret = ap.ArgumentParser(description="Skin combiner.")
    ret.add_argument("config", help="config file to use", nargs="?")
    ret.add_argument("-o", "--output", type=str, default="output.png", dest="output",
            help="output image file name, defaults to 'output.png'")
    return ret

def retrieve_skin_net(username):
    """Retrieves the player skin using the Mojang API and adds it to `SKINS`.

    Args:
        username: The player username.

    Returns:
        The `Skin` object generated from the skin.

    Raises:
        ValueError: If `username` is bad or no internet.
    """
    if username in SKINS:
        return SKINS[username]

    try:
        url = "https://api.mojang.com/users/profiles/minecraft/" + username
        with req.urlopen(url) as r:
            uuid = json.loads(r.read().decode("utf-8"))["id"]

        url = "https://sessionserver.mojang.com/session/minecraft/profile/" + uuid
        with req.urlopen(url) as r:
            prop = json.loads(r.read().decode("utf-8"))["properties"][0]["value"]

        url = json.loads(base64.b64decode(prop))["textures"]["SKIN"]["url"]
        with req.urlopen(url) as r:
            arr = np.asarray(bytearray(r.read()), dtype=np.uint8)

        skin = Skin(cv2.imdecode(arr, cv2.IMREAD_UNCHANGED))
        SKINS[username] = skin
        return skin
    except:
        raise ValueError(f"bad internet or bad username: {username}")

def retrieve_skin_file(path):
    """Retrieves the player skin from a local file and adds it to `SKINS`.

    Args:
        path: The path to the skin image.

    Returns:
        The `Skin` object constructed from the skin image.

    Raises:
        ValueError: If the skin image is bad.
    """
    if path in SKINS:
        return SKINS[path]

    try:
        skin = Skin(cv2.imread(path, cv2.IMREAD_UNCHANGED))
        SKINS[path] = skin
        return skin
    except Exception as e:
        raise ValueError(f"bad file path: {path}")

def parse_line(line):
    """Parses a line from the file.

    Args:
        line: The line to parse.

    Returns:
        The `Skin` constructed, the portion specified in the line (in the form of y, x, h, w), and the
        original portion specified in the line. In most cases the original portion will be the same as
        the portion returned, but it can be different if we are mapping a portion in 32x64 into 64x64.

        For example, if the `lleg` portion is specified on a 32x64 skin, it will mapped to `rleg` instead.
        However, we still want to keep the `lleg` portion so we can map it to `lleg` in the output.

    Raises:
        ValueError: If shit goes bad.
    """
    split = line.split()    # [body, skin]
    if len(split) < 2:
        raise ValueError(f"bad line: {line}")

    split[0] = split[0].casefold()
    if split[0] not in SKIN_PORTION:
        raise ValueError(f"bad portion: {split[0]} (on line {line})")

    # ((y, x, h, w), 64 only, [32 equiv])
    pt, dest_pt = SKIN_PORTION[split[0]], SKIN_PORTION[split[0]]
    skin = retrieve_skin_file(split[1]) if split[1].endswith(".png") else retrieve_skin_net(split[1])
    if skin.is32 and pt[1] and (pt[2] is None):       # is skin portion supported?
        raise ValueError(f"skin {split[1]} doesn't have have {split[0]}")
    if skin.is32 and pt[1] and (pt[2] is not None):   # update portion if supported
        pt = SKIN_PORTION[pt[2]]
    return skin, pt[0], dest_pt[0]

def file_mode(file, outfile="output.png"):
    """Reads the whole config file and perform the actions.

    Args:
        file: The input file to read from.
        outfile: The output image filename, defaults to 'output.png'.

    Returns:
        The error message, if any.
    """
    try:
        output = np.zeros((64, 64, 4), np.uint8)
        with open(args.config, "r") as f:
            lines = f.readlines()

        for line in lines:
            line = line.strip()
            if not line:
                continue

            skin, pt, dest_pt = parse_line(line)
            y, x, h, w = dest_pt
            output[y:y + h, x:x + w] = skin.get_portion(pt)
        cv2.imwrite(outfile, output)
    except Exception as e:
        return f"ERROR: {e}"

def interactive_mode(outfile="output.png"):
    """Run in interactive mode.

    Args:
        outfile: The output image filename, defaults to 'output.png'.
    """
    output = np.zeros((64, 64, 4), np.uint8)
    while True:
        try:
            cmd = input("skinmash> ")
            if (cmd == "exit") or (cmd == "quit"):
                cv2.imwrite(outfile, output)
                return

            skin, pt, dest_pt = parse_line(cmd)
            y, x, h, w = dest_pt
            output[y:y + h, x:x + w] = skin.get_portion(pt)
        except Exception as e:
            print(f"ERROR: {e}")
        except (SystemExit, KeyboardInterrupt):     # save the image on CTRL+C
            cv2.imwrite(outfile, output)
            return

if __name__ == "__main__":
    args = get_args().parse_args()
    if args.config:
        err = file_mode(args.config, args.output)
        if err:
            print(err, file=sys.stderr)
            exit(1)
    else:       # no config, run in interactive
        interactive_mode(args.output)

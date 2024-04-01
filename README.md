# ImageLabeling
## Easy-Peazy
--------------
- Create a folder for your dataset: lastname-firstname
- `cd lastname-firstname`
- `git clone git@github.com:Chunt0/ImageLabeling.git`
- Move all images into `./static/target`
- Make sure you are in `./lastname-firstname` again
- `mv ImageLabeling/* ./`
- `rm -rf ImageLabeling/`
- `./handle_smalls.sh`
- Handle the smalls! Likely this will mean starting a ComfyUi session, drop the chimp.png photo into the ComfyUI workspace to load up the batch upsampling work flow
- Get the full path to the static/smalls directory and use that to begining batch upsampling. Run automatic queue in Comfy.
- Move the upsampled images into ./static/target
- Back in the project root directory
- `./target_prep.sh`
- `python3 app.py`
- Begin labeling! You should be able to leave at any time and return right where you left off. If you do leave, remember to turn off your app (ctrl+c in the terminal)
- Keep labeling until the monkey is reached. Once reached all renamed files should be in completed folder. All notes are in notes.txt in the project root folder.


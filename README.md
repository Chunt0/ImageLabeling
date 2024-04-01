# ImageLabeling Project Guide

Follow these instructions to ensure a smooth workflow.

## Initial Setup

1. **Prepare Your Dataset Folder:**
   - Create a new folder named using the pattern `lastname-firstname`.
   - Navigate into your newly created folder: `cd lastname-firstname`.

2. **Clone the Repository:**
   - Clone the ImageLabeling repository into your dataset folder:
     ```bash
     git clone git@github.com:Chunt0/ImageLabeling.git
     ```

3. **Organize Your Images:**
   - Move all your images into the `./static/target` directory within the cloned repository.
   - Ensure you're in the `./lastname-firstname` directory before proceeding.

4. **Integrate the Cloned Repository:**
   - Move all contents from the `ImageLabeling` directory to your dataset folder:
     ```bash
     mv ImageLabeling/* ./
     ```
   - Remove the now-empty `ImageLabeling` directory:
     ```bash
     rm -rf ImageLabeling/
     ```

## Image Processing

1. **Handle Small Images:**
   - Execute `./handle_smalls.sh` to sort out smaller images.
   - For small images, initiate a ComfyUi session and use the `chimp.png` photo in the ComfyUI workspace to start the batch upsampling workflow.

2. **Upsample Images:**
   - Determine the full path to the `static/smalls` directory for batch upsampling.
   - Utilize the automatic queue feature in ComfyUI for efficient processing.
   - Move the upsampled images back into `./static/target`.

## Image Labeling

1. **Prepare Target Images:**
   - Run `./target_prep.sh` from the project root directory to prepare images for labeling.

2. **Start Labeling Application:**
   - Launch the labeling application:
     ```bash
     python3 app.py
     ```
   - You can exit the application at any time with `CTRL+C` and resume where you left off.

3. **Complete Labeling:**
   - Continue labeling images until you reach the designated "monkey" marker.
   - Upon completion, all renamed files will be moved to the `completed` folder.
   - Any notes taken during the process should be saved in `notes.txt` in the project root folder.

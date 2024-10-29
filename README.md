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

3. **Integrate the Cloned Repository:**
   - Move all contents from the `ImageLabeling` directory to your dataset folder:
     ```bash
     mv ImageLabeling/* ./
     ```
   - Remove the now-empty `ImageLabeling` directory:
     ```bash
     rm -rf ImageLabeling/
     ```

4. **Move Images**
   - Move all images you want to label into `./static/target/`

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

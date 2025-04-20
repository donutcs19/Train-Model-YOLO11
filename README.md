# Train-Model-YOLO11

Link Github
https://github.com/ultralytics/ultralytics

Link Doc
https://docs.ultralytics.com/


## install command config graphic card (Use Anaconda >> https://www.anaconda.com/)
# Create env with conda
conda create --name yolo11 python=3.10
conda activate yolov11


## เริ่มจากตรงนี้
#1 Install the ultralytics package using conda
conda install -c conda-forge ultralytics=8.3.3

#2 Install all packages together using conda
conda install -c pytorch -c nvidia -c conda-forge pytorch torchvision pytorch-cuda=12.1 ultralytics=8.3.3

#3
conda install pytorch torchvision torchaudio pytorch-cuda=12.1 -c pytorch -c nvidia

#4
pip install opencv-contrib-python

#5
pip install shapely

#ถ้า cuda false ใช้อันนี้
pip uninstall torch torchvision torchaudio -y

pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121

#error
pip install --upgrade --force-reinstall numpy


#trainModel

step 1
https://app.roboflow.com/login

New Project 
Object Detection >> Project name : name, Annotation Group : ., License : CC BY 4.0
Create New Project
Select 15 image
Save and Continue
Start m/n label, total 15/15
Assign to myself
Draw image

step 2
add img to data step
split img..., train 70% valid 30% test 0%

step 3
Continue
Continue
Continue
Arg = Flip, Rotation, Blur, Hue, Brightness, noise  เพิ่มความแม่ยำ
Download Dataset >> Download zip to PC ,YOLOV11

step 4
Extract zip
Copy file to Project

step 5
run >> python 1-train.python
wait to train
train finish
test model >> python 1-show.py

enjoy^^






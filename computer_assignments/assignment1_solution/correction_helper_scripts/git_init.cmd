mkdir bak
mv *.h5 *.txt *.svg *.mp4 ./bak
cp ../G01/ca1_step1_input_data.txt .
git init
git add *.py
git commit -m "1st commit"

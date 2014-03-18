Base64 Skin Packager for JW Player
==========

This is a small Python Script for use with the JW Player. It will convert your JW Player source skin into a base64 encoded skin. 

Using this script:
==========

First, you need Python installed. I tested this against Python 3.3.0 for Windows. 

Second, you need your original skin on your computer. 

The script will look for the skin in a folder called "skins". 

The skin name will be whatever you named your skin.

Inside of your skin folder there should be a folder called "src", which contains all of the original source elements for the skin, as well as the skin xml file.

When you run the script, the base 64 encoded version of the skin will appear one level up, inside of the main skin folder.

Example use:
==========

Running this script can be done from any terminal / command line. Simply open up the folder where this script resides and call skin.py skinname, where skinname is the name of your actual skin.

I have included a sample skin called "five", in this package. To run this in the command line, the following command needs to be run:

<pre>
skin.py five
</pre>

This will create the base64 encoded skin in the "five" folder, one level down from the "src" folder.

It is possible to change the paths of where the skins reside, as well as where the base 64 encoded versions are published to.

This section is where to look for the skin source files, feel free to edit it to better suit your needs:

<pre>
basePath = 'skins'
skinName = sys.argv[1]
skinPath = basePath + '/' + skinName + '/src/' + skinName + '.xml'
</pre>

Same with the output path:

<pre>
outputPath = skinPath = basePath + '/' + skinName + '/' + skinName + '.xml'
</pre>

The source code is available for this script. There is just a .py file for Python. Publishing the Python can be simply done with any text editor. Enjoy~! :)

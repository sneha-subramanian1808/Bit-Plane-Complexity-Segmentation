# BPCS-Project
##Embedding Function:

The Embed function uses Pillow to open the -i (vessel) and -s (secret) files and represents them
with Numpy uint8 matrices of height x width.

After that, the programme slices both matrices into x8 bitplane matrices. Bitplane secret files are completely sliced into 8x8's and queued before moving on to embedding
and error checks to confirm that the secret was large enough to embed. From left to right, top to bottom, least significant to most significant, the programme iterates
through each 9x9 square vessel until the queue is empty. At each 9x9, the complexity of the top-left corner 8x8 is checked, and if it is high enough, the 8x8 is overwritten with metadata, or the next 8x8 from queue, with the last bith set to 0 to indicate the data has not yet been checkerboarded.

After writing, the programme examines the newly written 8x8 complexity and, if it is not greater than the complexity threshold, it xors the 8x8 with a checkerboard to assure complexity and sets the last bit to 1 to indicate to decode.py that this square needs to be uncheckerboarded. The software then checks to see whether the queue has been completely empty, and if it hasn't, it writes that the embedding failed because the vessel doesn't have enough noisy sectors to fit the entire hidden picture, and then exits.

Otherwise, saveArr turns the vessel's bitplane, which now contains embedded data, back to an uint8 matrix. Pillow is then used to turn the saveArr into an Image, which is then saved as embedded.bmp.

##Decoding Function:

This programme uses Pillow to open the -i file (vessel) and represents it with a numpy uint8 matrix of height x width. The programme then slices each of the uint8 matrices into bitplane matrices with height x width x 8 dimensions. The entire vessel is iterated tg=hrough the 9x9's, which check the complexity of 8x8 top-left corners from left to right, top to bottom, least significant to most significant, and queue any 9x9 with an 8x8 complexity more than 0.45. 

To build bitPlaneArr's dimensions and a counter for the elements to be placed in bitPlaneArr, the programme decodes the metadata provided in the first element in the queue from embed.py. The software then iterates through every position 8x8 in bitPlaneArr from left to right, top to bottom, least significant to most significant, retrieving the next 9x9 from queue, uncheckboarding if the last bit is 1, and writing the top-left corner 8x8 into bitPlaneArr. This is repeated until the total number of 8x8s placed equals the total number of 8x8s in the image. As may be seen from the first element's metadata.

Finally, the software turns bitPlaneArr into an uint8 matrix, saveArr, and uses Pillow to convert saveArr into an image, which is then saved as decoded.bmp.


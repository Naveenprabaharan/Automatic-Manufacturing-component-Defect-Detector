import cv2
import numpy as np
from PIL import Image
from skimage.metrics import structural_similarity

# import Images
def Document_Tampering_Detection(original,tampered):


    original = Image.open(original)
    tampered = Image.open(tampered)

# size of images
    print("Original size:", original.size)
    print("Tamperd size:", tampered.size)

# Printing the image Formats
    print("Original format:", original.format)
    print("Tamperd format:", tampered.format)

# resize the Image to perform comparision
    original = original.resize((250, 160))
    tampered = tampered.resize((250, 160))

# After resize of images
    print("Original size:", original.size)
    print("Tamperd size:", tampered.size)


    original_gray = cv2.cvtColor(np.float32(original), cv2.COLOR_BGR2GRAY)
    tampered_gray = cv2.cvtColor(np.float32(tampered), cv2.COLOR_BGR2GRAY)

# finding structural_similarity between two pictures
    (score, diff) = structural_similarity(original_gray, tampered_gray, full=True)
    diff = (255 * diff).astype('uint8')
    score = score *100
    if (score >= 98):
        return "Prodect has Expected Accuracy - Ready for packing",score
    else:
        return "Prodect has less Accuracy - Defect",score

    return

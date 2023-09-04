import numpy as np
import cv2


def computeH(x1, x2):
    #Q2.2.1
    # TODO: Compute the homography between two sets of points




    return H2to1


def computeH_norm(x1, x2):
    #Q2.2.2
    # TODO: Compute the centroid of the points


    # TODO: Shift the origin of the points to the centroid


    # TODO: Normalize the points so that the largest distance from the origin is equal to sqrt(2)


    # TODO: Similarity transform 1


    # TODO: Similarity transform 2


    # TODO: Compute homography


    # TODO: Denormalization
    

    return H2to1




def computeH_ransac(locs1, locs2, opts):
    #Q2.2.3
    #Compute the best fitting homography given a list of matching points
    max_iters = opts.max_iters  # the number of iterations to run RANSAC for
    inlier_tol = opts.inlier_tol # the tolerance value for considering a point to be an inlier

    


    return bestH2to1, inliers



def compositeH(H2to1, template, img):
    
    #Create a composite image after warping the template image on top
    #of the image using the homography

    #Note that the homography we compute is from the image to the template;
    #x_template = H2to1*x_photo
    #For warping the template to the image, we need to invert it.
    

    # TODO: Create mask of same size as template

    # TODO: Warp mask by appropriate homography

    # TODO: Warp template by appropriate homography

    # TODO: Use mask to combine the warped template and the image
    
    return composite_img



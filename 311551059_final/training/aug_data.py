import Augmentor

TASK = "task3"
path = "C:\\Users\\yucheng\\Desktop\\PR_final\\dataset\\train\\" + TASK

def distortion(mag, num):
    p = Augmentor.Pipeline(path)
    p.ground_truth(path)
    p.zoom(probability=0.5, min_factor=1.05, max_factor=1.05)
    p.random_distortion(probability=1, grid_width=6, grid_height=2, magnitude=mag)
    p.sample(num)
    
def skew_tilt(num):
    p = Augmentor.Pipeline(path)
    p.skew_tilt(probability=0.5,magnitude=0.02)
    p.skew_left_right(probability=0.5,magnitude=0.02)
    p.skew_top_bottom(probability=0.5, magnitude=0.02)
    p.skew_corner(probability=0.5, magnitude=0.02)
    p.sample(num)
    

def rotate(num):
    p = Augmentor.Pipeline(path)
    p.rotate(probability=1,max_left_rotation=1,max_right_rotation=1)
    p.sample(num)
    

distortion(1, 12000)
distortion(2, 12000)
distortion(3, 12000)
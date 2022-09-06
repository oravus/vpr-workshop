import cv2
from pathlib import Path

path = Path("../assets/img/")
imgNames = path.glob('*')
skipNamesList = ['worldmap.jpg','vpr-workshop-banner-1.svg']
size = 400
savePath = path/'adapted'
savePath.mkdir(exist_ok=True)

for n in imgNames:
    if n.match('*logo*') or  n.name in skipNamesList or n.is_dir():
        continue
    else:
        # load
        print(f'Loading {n}')
        img = cv2.imread(str(n))

        # resize
        h,w = img.shape[:2]
        print(h,w)
        scale = size/h if w > h else size/w
        img = cv2.resize(img,None,fy=scale,fx=scale,interpolation=cv2.INTER_AREA)

        # center-crop
        h,w = img.shape[:2]
        hs = size//2 # halfsize
        img = img[h//2-hs:h//2+hs,w//2-hs:w//2+hs]

        # write
        print(savePath/n.name)
        cv2.imwrite(str(savePath/n.name),img)

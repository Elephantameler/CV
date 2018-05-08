from skimage import io
import numpy as np
import os as os

class CAS_util(object):
    """
    摘要:
        人脸图像数据库是人脸识别算法研究、开发、评测的基础，具有重要的意义。
        本文介绍了我们创建并已经部分共享的CAS-PEAL大规模中国人脸图像数据库及其基准测试结果。
        CAS-PEAL人脸库包含了1,040名中国人共99,450幅头肩部图像。
        所有图像在专门的采集环境中采集，涵盖了姿态、表情、饰物和光照四种主要变化条件，
        部分人脸图像具有背景、距离和时间跨度的变化。目前该人脸库的标准训练、测试子库已经公开发布。
        与其他已经公开发布的人脸库相比，CAS-PEAL人脸数据库在人数、图像变化条件等方面具有综合优势，
        将对人脸识别算法的研究、评测产生积极的影响。同时作为以东方人为主的人脸库，
        CAS-PEAL人脸库也使人脸识别算法在不同人种之间的比较成为可能，利于人脸识别算法在国内的实用化。
    """
    def __init__(self, path):
        """
        path: 数据集的绝对路径
        """
        self.path = path

    def load_training_set_image_name(self):
        """
        训练集合（Training Set）：除了模板匹配等少数简单算法，多数人脸识别算法都是需要进行训练的。
        因此，我们从正面子库中随机选择300人，每人随机选择4幅正面图像，共1,200幅图像构成训练集.

        outputs:
        - image_paths: 训练集的图片名称的一维数组 image_paths.shape = (N, )
        """
        path = self.path + 'TrainSet/nopreprocessed/raw/Trainingset'
        image_paths = []
        for i in os.walk(path):
            image_paths.append(i)
        #endfor
        return image_paths


    def load_gallery_image_name(self):
        """
        Gallery包含1,040人，每人1幅标准正面图像（正面平视，环境光照，中性表情，无饰物）

        outputs:
        - image_paths: 训练集的图片名称的一维数组 image_paths.shape = (N, )
        """
        path = self.path + 'TargetSet/nopreprocessed/raw/gallery'
        image_paths = []
        for i in os.walk(path):
            image_paths.append(i)
        #endfor
        return image_paths


    def load_Probe_Sets_image_name(self, mode=None):
        """

        Probe Sets包括除去训练集和原型集以外余下的6,992幅图像，
        分为表情变化、光照变化、饰物变化、背景变化、距离变化和时间跨度变化6个子集；
        表情子库: 环境光照模式下，要求志愿者做出笑、皱眉、惊讶、闭眼、张嘴5种表情
        饰物子库: 环境光照模式下，志愿者佩戴3种不同的帽子和3种不同的眼镜
        光照子库: 环境光源关闭，每次打开一个方向光源进行图片采集,上中下各5个角度光源
        背景子库: 5种不同的背景颜色包括蓝色、红色、黑色、白色和黄色
        距离子库: 环境光照模式下，改变志愿者与摄像头的相对距离，获取到距离子库中每个志愿者的3种不同距离的面部图像
        时间跨度子库: 随着时间的改变，人的面部特征会有一定的变化。在我们的人脸数据库中，
                     我们引入了时间跨度子库，子库中的志愿者图片距离他们第一次采集的图片有6个月的时间跨度
        Input:
        - mode(String):
                        Accessory: 饰物变化
                        Aging: 时间跨度变化
                        Background: 背景变化
                        Distance: 距离变换
                        Expression: 表情变化
                        Lighting: 光照变换


        outputs:
        - image_paths: 训练集的图片名称的一维数组 image_paths.shape = (N, )

        """

        path = self.path +'LightingSet/nopreprocessed/raw/LightingSet'

        image_paths = []
        for i in os.walk(path):
            image_paths.append(i)
        #endfor
        return image_paths


    def load_images(self, image_paths):
        """
        Inputs:
        - image_paths: 训练集的图片名称的一维数组 image_paths.shape = (N, )

        outputs:
        - images: numpy类型的图片缓存 images.shape = (N, 480, 360)

        """
        images = []
        for Path in image_paths:
            image = io.imread(self.path + "\\" + Path)
            images.append(image)
        images = np.array(images)
        return images

    #将诉诸
    def convert_array_to_image(arr, height=128, width=128):  
        img=[]  
        for i in range(height):  
            img.append(arr[i*width:i*width+width])  
        #endfor  
        return array(img)


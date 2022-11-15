from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, Flatten, MaxPooling2D, Dense, Dropout, BatchNormalization, Activation
from tensorflow.keras.preprocessing import image
import numpy as np
import urllib.request

categories = {0: '0.其他垃圾一次性快餐盒', 1: '1.其他垃圾污损塑料', 2: '2.其他垃圾烟蒂', 3: '3.其他垃圾牙签',
              4: '4.其他垃圾破碎花盆及碟碗', 5: '5.其他垃圾竹筷', 6: '6.厨余垃圾剩饭剩菜7.大骨头',
              7: '8.厨余垃圾水果果皮',
              8: '9.厨余垃圾水果果肉', 9: '10.厨余垃圾茶叶渣', 10: '11.厨余垃圾菜叶菜根', 11: '12.厨余垃圾蛋壳',
              12: '13.厨余垃圾鱼骨', 13: '14.可回收物充电宝', 14: '15.可回收物包', 15: '16.可回收物化妆品瓶',
              16: '17.可回收物塑料玩具', 17: '18.可回收物塑料碗盆', 18: '19.可回收物塑料衣架',
              19: '20.可回收物快递纸袋',
              20: '21.可回收物插头电线', 21: '22.可回收物旧衣服', 22: '23.可回收物易拉罐', 23: '24.可回收物枕头',
              24: '25.可回收物毛绒玩具', 25: '26.可回收物洗发水瓶', 26: '27.可回收物玻璃杯',
              27: '28.可回收物皮鞋', 28: '29.可回收物砧板', 29: '30.可回收物纸板箱', 30: '31.可回收物调料瓶',
              31: '32.可回收物酒瓶', 32: '33.可回收物金属食品罐', 33: '34.可回收物锅', 34: '35.可回收物食用油桶',
              35: '36.可回收物饮料瓶', 36: '37.有害垃圾干电池', 37: '38.有害垃圾软膏', 38: '39.有害垃圾过期药物'}

model_path = "huawei_garbage.h5"

# 加载模型h5文件
# model = load_model(model_path)

# Build Model
model = Sequential([
    Conv2D(filters=32, kernel_size=3, padding='same', activation='relu', input_shape=(300, 300, 3)),
    MaxPooling2D(pool_size=2),
    Conv2D(filters=64, kernel_size=3, padding='same', activation='relu'),
    MaxPooling2D(pool_size=2),
    Conv2D(filters=32, kernel_size=3, padding='same', activation='relu'),
    MaxPooling2D(pool_size=2),
    Conv2D(filters=32, kernel_size=3, padding='same', activation='relu'),
    MaxPooling2D(pool_size=2),
    Flatten(),
    Dense(64, activation='relu'),
    Dense(39, activation='softmax')
])

model.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['acc'])

model.load_weights(model_path)


def predict_image(imgName):
    img = image.load_img('D:\\StudyAndWork\\GitRepository\\GarageRecognitionBackend\\upload\\images\\%s' % str(imgName))
    img = img.resize((300, 300))
    x = image.img_to_array(img)
    x /= 255
    x = np.expand_dims(x, axis=0)
    y = model.predict(x)
    i = np.argmax(y[0])
    return categories[i][3:7]

# print(predict_image('D:\\StudyAndWork\\GitRepository\\RecognitionModel\\test.jpg'))
# print(predict_image('http://127.0.0.1:8081/images/1edb58c91df24e1c8f7e843b98ef9f91.jpg'))

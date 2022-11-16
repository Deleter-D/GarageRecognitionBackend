from tensorflow.keras.models import load_model
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, Flatten, MaxPooling2D, Dense, Dropout, BatchNormalization
import numpy as np
from tensorflow.keras.preprocessing import image
from tensorflow.keras.layers import Input, concatenate, AveragePooling2D, GlobalAveragePooling2D
from tensorflow.keras import Model

categories = {0: '其他垃圾', 1: '厨余垃圾', 2: '可回收物', 3: '有害垃圾'}

model_path = "huawei_garbage.h5"

# 加载模型h5文件
# model = load_model(model_path)

# Build Model
IMSIZE = 299
input_layer = Input([IMSIZE, IMSIZE, 3])
x = input_layer

x = Conv2D(32, (3, 3), strides=(2, 2), padding='valid', activation='relu')(x)
x = Conv2D(32, (3, 3), strides=(1, 1), padding='valid', activation='relu')(x)
x = Conv2D(64, (3, 3), strides=(2, 2), padding='same', activation='relu')(x)
x = MaxPooling2D(pool_size=(3, 3), strides=(2, 2), padding='same')(x)

x = BatchNormalization(axis=3)(x)
x = Conv2D(80, (3, 3), strides=(1, 1), padding='valid', activation='relu')(x)
x = Conv2D(96, (3, 3), strides=(1, 1), padding='valid', activation='relu')(x)
x = MaxPooling2D(pool_size=(3, 3), strides=(2, 2), padding='same')(x)

# inception moduleA1
inception_3a_1_1 = Conv2D(64, (1, 1), strides=(1, 1), padding='same', activation='relu')(x)  # 第一个分支64通道的1*1卷积

# 第二个分支48通道1*1卷积后一层链接一个64通道的5*5卷积
inception_3a_3_3_reduce = Conv2D(48, (1, 1), strides=(1, 1), padding='same', activation='relu')(x)
inception_3a_3_3 = Conv2D(64, (5, 5), strides=(1, 1), padding='same', activation='relu')(inception_3a_3_3_reduce)

# 第三个分支64通道1*1卷积后一层链接2个96通道的5*5卷积
inception_3a_5_5_reduce = Conv2D(64, (1, 1), strides=(1, 1), padding='same', activation='relu')(x)
inception_3a_5_5_asym_1 = Conv2D(96, (3, 3), strides=(1, 1), padding='same', activation='relu')(inception_3a_5_5_reduce)
inception_3a_5_5 = Conv2D(96, (3, 3), strides=(1, 1), padding='same', activation='relu')(inception_3a_5_5_asym_1)

# 第四个分支为3*3的平均池化后一层连接32通道的1*1卷积
inception_3a_pool = AveragePooling2D(pool_size=(3, 3), strides=(1, 1), padding='same')(x)
inception_3a_pool_1_1 = Conv2D(32, (1, 1), strides=(1, 1), padding='same', activation='relu')(inception_3a_pool)

inception_3a_output = concatenate([inception_3a_1_1, inception_3a_3_3, inception_3a_5_5, inception_3a_pool_1_1], axis=3)
# inception moduleA2
# 同样有4个分支，唯一不同的是第4个分支最后接的是64输出通道
inception_3a2_1_1 = Conv2D(64, (1, 1), strides=(1, 1), padding='same', activation='relu')(
    inception_3a_output)  # 第一个分支64通道的1*1卷积

inception_3a2_3_3_reduce = Conv2D(48, (1, 1), strides=(1, 1), padding='same', activation='relu')(inception_3a_output)
inception_3a2_3_3 = Conv2D(64, (5, 5), strides=(1, 1), padding='same', activation='relu')(inception_3a2_3_3_reduce)

inception_3a2_5_5_reduce = Conv2D(64, (1, 1), strides=(1, 1), padding='same', activation='relu')(inception_3a_output)
inception_3a2_5_5_asym_1 = Conv2D(96, (3, 3), strides=(1, 1), padding='same', activation='relu')(
    inception_3a2_5_5_reduce)
inception_3a2_5_5 = Conv2D(96, (3, 3), strides=(1, 1), padding='same', activation='relu')(inception_3a2_5_5_asym_1)

inception_3a2_pool = AveragePooling2D(pool_size=(3, 3), strides=(1, 1), padding='same')(inception_3a_output)
inception_3a2_pool_1_1 = Conv2D(64, (1, 1), strides=(1, 1), padding='same', activation='relu')(inception_3a2_pool)

inception_3a2_output = concatenate([inception_3a2_1_1, inception_3a2_3_3, inception_3a2_5_5, inception_3a2_pool_1_1],
                                   axis=3)
# inception moduleA3
inception_3a3_1_1 = Conv2D(64, (1, 1), strides=(1, 1), padding='same', activation='relu')(
    inception_3a2_output)  # 第一个分支64通道的1*1卷积

inception_3a3_3_3_reduce = Conv2D(48, (1, 1), strides=(1, 1), padding='same', activation='relu')(inception_3a2_output)
inception_3a3_3_3 = Conv2D(64, (5, 5), strides=(1, 1), padding='same', activation='relu')(inception_3a2_3_3_reduce)

inception_3a3_5_5_reduce = Conv2D(64, (1, 1), strides=(1, 1), padding='same', activation='relu')(inception_3a2_output)
inception_3a3_5_5_asym_1 = Conv2D(96, (3, 3), strides=(1, 1), padding='same', activation='relu')(
    inception_3a3_5_5_reduce)
inception_3a3_5_5 = Conv2D(96, (3, 3), strides=(1, 1), padding='same', activation='relu')(inception_3a3_5_5_asym_1)

inception_3a3_pool = AveragePooling2D(pool_size=(3, 3), strides=(1, 1), padding='same')(inception_3a2_output)
inception_3a3_pool_1_1 = Conv2D(64, (1, 1), strides=(1, 1), padding='same', activation='relu')(inception_3a3_pool)

inception_3a3_output = concatenate([inception_3a3_1_1, inception_3a3_3_3, inception_3a3_5_5, inception_3a3_pool_1_1],
                                   axis=3)

# inception moduleB1
inception_B1_1_1 = Conv2D(384, (3, 3), strides=(2, 2), padding='valid', activation='relu')(
    inception_3a3_output)  # 第一个分支64通道的1*1卷积

# 64通道的1*1加2个96通道的3*3卷积
inception_B1_3_3_reduce = Conv2D(64, (1, 1), strides=(1, 1), padding='same', activation='relu')(inception_3a3_output)
inception_B1_3_3_asym_1 = Conv2D(96, (3, 3), strides=(1, 1), padding='same', activation='relu')(inception_B1_3_3_reduce)
inception_B1_3_3 = Conv2D(96, (3, 3), strides=(2, 2), padding='valid', activation='relu')(inception_B1_3_3_asym_1)

inception_B1_pool = MaxPooling2D(pool_size=(3, 3), strides=(2, 2), padding='valid')(inception_3a3_output)

inception_B1_output = concatenate([inception_B1_1_1, inception_B1_3_3, inception_B1_pool], axis=3)

# inception moduleB2
inception_B2_1_1 = Conv2D(192, (1, 1), strides=(1, 1), padding='same', activation='relu')(inception_B1_output)

inception_B2_3_3_reduce = Conv2D(128, (1, 1), strides=(1, 1), padding='same', activation='relu')(inception_B1_output)
inception_B2_3_3_asym_1 = Conv2D(128, (1, 7), strides=(1, 1), padding='same', activation='relu')(
    inception_B2_3_3_reduce)
inception_B2_3_3 = Conv2D(192, (7, 1), strides=(1, 1), padding='same', activation='relu')(inception_B2_3_3_asym_1)

inception_B2_3 = Conv2D(128, (1, 1), strides=(1, 1), padding='same', activation='relu')(inception_B1_output)
inception_B2_3_reduce = Conv2D(128, (7, 1), strides=(1, 1), padding='same', activation='relu')(inception_B2_3)
inception_B2_3_asym_1 = Conv2D(128, (1, 7), strides=(1, 1), padding='same', activation='relu')(inception_B2_3_reduce)
inception_B2_3_asym_2 = Conv2D(128, (7, 1), strides=(1, 1), padding='same', activation='relu')(inception_B2_3_asym_1)
inception_B2_3_asym_3 = Conv2D(192, (1, 7), strides=(1, 1), padding='same', activation='relu')(inception_B2_3_asym_2)

inception_B2_3_pool = AveragePooling2D(pool_size=(3, 3), strides=(1, 1), padding='same')(inception_B1_output)
inception_B2_3_pool_1_1 = Conv2D(192, (1, 1), strides=(1, 1), padding='same', activation='relu')(inception_B2_3_pool)

inception_B2_output = concatenate([inception_B2_1_1, inception_B2_3_3, inception_B2_3_asym_3, inception_B2_3_pool_1_1],
                                  axis=3)
# inception moduleB3
inception_B3_1_1 = Conv2D(192, (1, 1), strides=(1, 1), padding='same', activation='relu')(inception_B2_output)

inception_B3_3_3_reduce = Conv2D(160, (1, 1), strides=(1, 1), padding='same', activation='relu')(inception_B2_output)
inception_B3_3_3_asym_1 = Conv2D(162, (1, 7), strides=(1, 1), padding='same', activation='relu')(
    inception_B3_3_3_reduce)
inception_B3_3_3 = Conv2D(192, (7, 1), strides=(1, 1), padding='same', activation='relu')(inception_B3_3_3_asym_1)

inception_B3_3 = Conv2D(160, (1, 1), strides=(1, 1), padding='same', activation='relu')(inception_B2_output)
inception_B3_3_reduce = Conv2D(160, (7, 1), strides=(1, 1), padding='same', activation='relu')(inception_B3_3)
inception_B3_3_asym_1 = Conv2D(160, (1, 7), strides=(1, 1), padding='same', activation='relu')(inception_B3_3_reduce)
inception_B3_3_asym_2 = Conv2D(160, (7, 1), strides=(1, 1), padding='same', activation='relu')(inception_B3_3_asym_1)
inception_B3_3_asym_3 = Conv2D(192, (1, 7), strides=(1, 1), padding='same', activation='relu')(inception_B3_3_asym_2)

inception_B3_3_pool = AveragePooling2D(pool_size=(3, 3), strides=(1, 1), padding='same')(inception_B2_output)
inception_B3_3_pool_1_1 = Conv2D(192, (1, 1), strides=(1, 1), padding='same', activation='relu')(inception_B3_3_pool)

inception_B3_output = concatenate([inception_B3_1_1, inception_B3_3_3, inception_B3_3_asym_3, inception_B3_3_pool_1_1],
                                  axis=3)
# inception moduleB4
inception_B4_1_1 = Conv2D(192, (1, 1), strides=(1, 1), padding='same', activation='relu')(inception_B3_output)

inception_B4_3_3_reduce = Conv2D(160, (1, 1), strides=(1, 1), padding='same', activation='relu')(inception_B3_output)
inception_B4_3_3_asym_1 = Conv2D(162, (1, 7), strides=(1, 1), padding='same', activation='relu')(
    inception_B4_3_3_reduce)
inception_B4_3_3 = Conv2D(192, (7, 1), strides=(1, 1), padding='same', activation='relu')(inception_B4_3_3_asym_1)

inception_B4_3 = Conv2D(160, (1, 1), strides=(1, 1), padding='same', activation='relu')(inception_B3_output)
inception_B4_3_reduce = Conv2D(160, (7, 1), strides=(1, 1), padding='same', activation='relu')(inception_B4_3)
inception_B4_3_asym_1 = Conv2D(160, (1, 7), strides=(1, 1), padding='same', activation='relu')(inception_B4_3_reduce)
inception_B4_3_asym_2 = Conv2D(160, (7, 1), strides=(1, 1), padding='same', activation='relu')(inception_B4_3_asym_1)
inception_B4_3_asym_3 = Conv2D(192, (1, 7), strides=(1, 1), padding='same', activation='relu')(inception_B4_3_asym_2)

inception_B4_3_pool = AveragePooling2D(pool_size=(3, 3), strides=(1, 1), padding='same')(inception_B3_output)
inception_B4_3_pool_1_1 = Conv2D(192, (1, 1), strides=(1, 1), padding='same', activation='relu')(inception_B4_3_pool)

inception_B4_output = concatenate([inception_B4_1_1, inception_B4_3_3, inception_B4_3_asym_3, inception_B4_3_pool_1_1],
                                  axis=3)
# inception moduleB5
inception_B5_1_1 = Conv2D(192, (1, 1), strides=(1, 1), padding='same', activation='relu')(inception_B4_output)

inception_B5_3_3_reduce = Conv2D(160, (1, 1), strides=(1, 1), padding='same', activation='relu')(inception_B4_output)
inception_B5_3_3_asym_1 = Conv2D(162, (1, 7), strides=(1, 1), padding='same', activation='relu')(
    inception_B5_3_3_reduce)
inception_B5_3_3 = Conv2D(192, (7, 1), strides=(1, 1), padding='same', activation='relu')(inception_B5_3_3_asym_1)

inception_B5_3 = Conv2D(160, (1, 1), strides=(1, 1), padding='same', activation='relu')(inception_B4_output)
inception_B5_3_reduce = Conv2D(160, (7, 1), strides=(1, 1), padding='same', activation='relu')(inception_B5_3)
inception_B5_3_asym_1 = Conv2D(160, (1, 7), strides=(1, 1), padding='same', activation='relu')(inception_B5_3_reduce)
inception_B5_3_asym_2 = Conv2D(160, (7, 1), strides=(1, 1), padding='same', activation='relu')(inception_B5_3_asym_1)
inception_B5_3_asym_3 = Conv2D(192, (1, 7), strides=(1, 1), padding='same', activation='relu')(inception_B5_3_asym_2)

inception_B5_3_pool = AveragePooling2D(pool_size=(3, 3), strides=(1, 1), padding='same')(inception_B4_output)
inception_B5_3_pool_1_1 = Conv2D(192, (1, 1), strides=(1, 1), padding='same', activation='relu')(inception_B5_3_pool)

inception_B5_output = concatenate([inception_B5_1_1, inception_B5_3_3, inception_B5_3_asym_3, inception_B5_3_pool_1_1],
                                  axis=3)
# inception moduleC1
inception_C1_1_1 = Conv2D(192, (1, 1), strides=(1, 1), padding='same', activation='relu')(
    inception_B5_output)  # 第一个分支64通道的1*1卷积
inception_C1 = Conv2D(320, (3, 3), strides=(2, 2), padding='valid', activation='relu')(inception_C1_1_1)
# 64通道的1*1加2个96通道的3*3卷积
inception_C1_3 = Conv2D(192, (1, 1), strides=(1, 1), padding='same', activation='relu')(inception_B5_output)
inception_C1_3_reduce = Conv2D(192, (7, 1), strides=(1, 1), padding='same', activation='relu')(inception_C1_3)
inception_C1_3_asym_1 = Conv2D(192, (1, 7), strides=(1, 1), padding='same', activation='relu')(inception_C1_3_reduce)
inception_C1_3_asym_2 = Conv2D(192, (3, 3), strides=(2, 2), padding='valid', activation='relu')(inception_C1_3_asym_1)

inception_C1_pool = MaxPooling2D(pool_size=(3, 3), strides=(2, 2), padding='valid')(inception_B5_output)

inception_C1_output = concatenate([inception_C1, inception_C1_3_asym_2, inception_C1_pool], axis=3)
# inception moduleC2
inception_C2_1_1 = Conv2D(320, (1, 1), strides=(1, 1), padding='same', activation='relu')(inception_C1_output)

inception_C2_3 = Conv2D(384, (1, 1), strides=(1, 1), padding='same', activation='relu')(inception_C1_output)
inception_C2_3_asym_1 = Conv2D(384, (1, 3), strides=(1, 1), padding='same', activation='relu')(inception_C2_3)
inception_C2_3_asym_2 = Conv2D(384, (3, 1), strides=(1, 1), padding='same', activation='relu')(inception_C2_3)
inception_C2_3_concat = concatenate([inception_C2_3_asym_1, inception_C2_3_asym_2], axis=3)

inception_C21_3 = Conv2D(448, (1, 1), strides=(1, 1), padding='same', activation='relu')(inception_C1_output)
inception_C21_31 = Conv2D(384, (3, 3), strides=(1, 1), padding='same', activation='relu')(inception_C21_3)
inception_C21_3_asym_1 = Conv2D(384, (1, 3), strides=(1, 1), padding='same', activation='relu')(inception_C21_31)
inception_C21_3_asym_2 = Conv2D(384, (3, 1), strides=(1, 1), padding='same', activation='relu')(inception_C21_31)
inception_C21_3_concat = concatenate([inception_C21_3_asym_1, inception_C21_3_asym_2], axis=3)

inception_C22_3_pool = AveragePooling2D(pool_size=(3, 3), strides=(1, 1), padding='same')(inception_C1_output)
inception_C22_3_pool_1 = Conv2D(192, (1, 1), strides=(1, 1), padding='same', activation='relu')(inception_C22_3_pool)

inception_C2_output = concatenate(
    [inception_C2_1_1, inception_C2_3_concat, inception_C21_3_concat, inception_C22_3_pool_1], axis=3)
# inception moduleC3
inception_C3_1_1 = Conv2D(320, (1, 1), strides=(1, 1), padding='same', activation='relu')(inception_C2_output)

inception_C3_3 = Conv2D(384, (1, 1), strides=(1, 1), padding='same', activation='relu')(inception_C2_output)
inception_C3_3_asym_1 = Conv2D(384, (1, 3), strides=(1, 1), padding='same', activation='relu')(inception_C3_3)
inception_C3_3_asym_2 = Conv2D(384, (3, 1), strides=(1, 1), padding='same', activation='relu')(inception_C3_3)
inception_C3_3_concat = concatenate([inception_C2_3_asym_1, inception_C2_3_asym_2], axis=3)

inception_C31_3 = Conv2D(448, (1, 1), strides=(1, 1), padding='same', activation='relu')(inception_C2_output)
inception_C31_31 = Conv2D(384, (3, 3), strides=(1, 1), padding='same', activation='relu')(inception_C31_3)
inception_C31_3_asym_1 = Conv2D(384, (1, 3), strides=(1, 1), padding='same', activation='relu')(inception_C31_31)
inception_C31_3_asym_2 = Conv2D(384, (3, 1), strides=(1, 1), padding='same', activation='relu')(inception_C31_31)
inception_C31_3_concat = concatenate([inception_C21_3_asym_1, inception_C21_3_asym_2], axis=3)

inception_C32_3_pool = AveragePooling2D(pool_size=(3, 3), strides=(1, 1), padding='same')(inception_C2_output)
inception_C32_3_pool_1 = Conv2D(192, (1, 1), strides=(1, 1), padding='same', activation='relu')(inception_C22_3_pool)

x = concatenate([inception_C3_1_1, inception_C3_3_concat, inception_C31_3_concat, inception_C32_3_pool_1], axis=3)

x = GlobalAveragePooling2D()(x)

x = Dropout(0.4)(x)
x = Flatten()(x)
x = Dense(4, activation='sigmoid')(x)
output_layer = x
model = Model(input_layer, output_layer)

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

model.load_weights(model_path)


def predict_image(imgName):
    img = image.load_img('D:\\StudyAndWork\\GitRepository\\GarageRecognitionBackend\\upload\\images\\%s' % str(imgName))
    img = img.resize((IMSIZE, IMSIZE))
    x = image.img_to_array(img)
    x /= 255
    x = np.expand_dims(x, axis=0)
    y = model.predict(x)
    i = np.argmax(y)
    return categories[i]


# print(predict_image('1edb58c91df24e1c8f7e843b98ef9f91.jpg'))

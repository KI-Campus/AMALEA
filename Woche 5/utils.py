import glob
import os

from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

import keras
from keras import backend as K

from keras.layers import UpSampling2D
from keras.layers import Conv2DTranspose
from keras.layers import Input, BatchNormalization
from keras.models import Model

rgb_array = np.load("data/dataset/rgb_array.npy")


class LossGraph(keras.callbacks.Callback):

    """Custom Callback to visualize accuracy or loss at the end of training."""

    def __init__(self, acc_or_loss):
        super(LossGraph, self).__init__()
        self.acc_or_loss = acc_or_loss

    def on_train_begin(self, logs={}):
        self.train_loss = []
        self.val_loss = []
        self.train_acc = []
        self.val_acc = []
        self.epoch_count = 0

    def on_epoch_end(self, batch, logs={}):

        self.epoch_count += 1
        self.train_loss.append(logs.get("loss"))
        self.val_loss.append(logs.get("val_loss"))
        self.train_acc.append(logs.get("acc"))
        self.val_acc.append(logs.get("val_acc"))

    def on_train_end(self, logs={}):

        x = np.arange(1, len(self.train_loss) + 1)

        if self.acc_or_loss == "acc":
            plt.plot(x, self.train_acc, "ro", label="Train_accuracy")
            plt.plot(x, self.val_acc, "go", label="Val_accuracy")
            plt.legend()
            plt.title(
                "Training and Validation Accuracy for "
                + str(self.epoch_count)
                + " epochs of training."
            )
        elif self.acc_or_loss == "loss":
            plt.plot(x, self.train_loss, "ro", label="Train_loss")
            plt.plot(x, self.val_loss, "go", label="Val_loss")
            plt.legend()
            plt.title(
                "Training and Validation Loss for "
                + str(self.epoch_count)
                + " epochs of training."
            )
        plt.show()


def get_output(model, layer_name, model_input):

    """Function to set model into learning phase and get
    model activations after feedforward pass to visualize activations"""

    get_act = K.function(
        [model.layers[0].input, K.learning_phase()],
        [model.get_layer(layer_name).output],
    )
    act = get_act([model_input])[0]
    return act


def transform_into_bitmap(images, classes_list):

    new_shape = list(images.shape[:3])
    new_shape.append(len(classes_list))

    images_as_classes = np.zeros(new_shape, np.uint8)
    print("Bitmap is of shape", images_as_classes.shape)
    i = 0
    for image in range(0, images.shape[0]):
        i = i + 1
        if image % 10 == 0 and image != 0:
            print(
                str(i - 1)
                + " of "
                + str(images.shape[0])
                + " done. please hold the line."
            )

        for row in range(0, images.shape[1]):
            for column in range(0, images.shape[2]):

                index = classes_list.index(list(images[image, row, column, :]))
                images_as_classes[image, row, column, index] = 1

    print("done")

    return images_as_classes


def augment_images(images, h_flip=True, rotate180=True, shift_random=True):

    """Augmenting images with numpy functions, so that it
    is not needed to use the generator function."""

    np.random.seed(0)

    if h_flip:

        images_h_flip = np.zeros(images.shape).astype("uint8")

        for nb_sample in range(0, images.shape[0], 1):

            images_h_flip[nb_sample, :, :, :] = np.fliplr(images[nb_sample, :, :, :])

        images = np.vstack((images, images_h_flip))

    print("stage1")

    if rotate180:

        images_rot180 = np.zeros(images.shape).astype("uint8")

        for nb_sample in range(0, images.shape[0], 1):

            images_rot180[nb_sample, :, :, :] = np.rot90(images[nb_sample, :, :, :], 2)

        images = np.vstack((images, images_rot180))

    print("stage2")

    if shift_random:

        shift_images = np.zeros(images.shape).astype("uint8")

        for nb_sample in range(0, images.shape[0], 1):

            shift_images[nb_sample, :, :, :] = np.roll(
                images[nb_sample, :, :, :],
                np.random.randint(images.shape[2]),
                np.random.randint(0, 2),
            )

        images = np.vstack((images, shift_images))

    print("done")

    return images


def get_prediction(predicted_bitmap, classes_list):

    """Function to transform bitmaps prediction into RGB image"""

    new_shape = list(predicted_bitmap.shape[1:3])
    new_shape.append(3)
    image = np.zeros(new_shape).astype("uint8")

    for nb_image in range(0, predicted_bitmap.shape[0]):
        for row in range(0, predicted_bitmap.shape[1]):
            for column in range(0, predicted_bitmap.shape[2]):

                class_index = np.argmax(
                    predicted_bitmap[nb_image, row, column, :], axis=0
                )
                rgb_value = classes_list[class_index]

                image[row, column, 0] = int(float(rgb_value[0]))
                image[row, column, 1] = int(float(rgb_value[1]))
                image[row, column, 2] = int(float(rgb_value[2]))

    return image


def build_ae(vgg16_encoder, x_train_shape, class_or_regr):

    """Build your autoencoder in here."""

    encoder_input = Input(shape=x_train_shape, name="encoder_input")

    # ---------- block1

    x = vgg16_encoder.get_layer("block1_conv1")(encoder_input)
    x = BatchNormalization()(x)
    x = vgg16_encoder.get_layer("block1_conv2")(x)
    x = BatchNormalization()(x)
    x = vgg16_encoder.get_layer("block1_pool")(x)

    # ---------- block2

    x = vgg16_encoder.get_layer("block2_conv1")(x)
    x = BatchNormalization()(x)
    x = vgg16_encoder.get_layer("block2_conv2")(x)
    x = BatchNormalization()(x)
    x = vgg16_encoder.get_layer("block2_pool")(x)

    # ---------- block3

    x = vgg16_encoder.get_layer("block3_conv1")(x)
    x = BatchNormalization()(x)
    x = vgg16_encoder.get_layer("block3_conv2")(x)
    x = BatchNormalization()(x)
    x = vgg16_encoder.get_layer("block3_conv3")(x)
    x = BatchNormalization()(x)
    x = vgg16_encoder.get_layer("block3_pool")(x)

    # ---------- block4

    x = vgg16_encoder.get_layer("block4_conv1")(x)
    x = BatchNormalization()(x)
    x = vgg16_encoder.get_layer("block4_conv2")(x)
    x = BatchNormalization()(x)
    x = vgg16_encoder.get_layer("block4_conv3")(x)
    x = BatchNormalization()(x)
    x = vgg16_encoder.get_layer("block4_pool")(x)

    # ---------- block5

    x = vgg16_encoder.get_layer("block5_conv1")(x)
    x = BatchNormalization()(x)
    x = vgg16_encoder.get_layer("block5_conv2")(x)
    x = BatchNormalization()(x)
    encoded = vgg16_encoder.get_layer("block5_conv3")(x)

    # ---------- block5
    x = Conv2DTranspose(512, (3, 3), activation="relu", padding="same")(encoded)
    x = BatchNormalization()(x)
    x = Conv2DTranspose(512, (3, 3), activation="relu", padding="same")(x)
    x = BatchNormalization()(x)
    x = Conv2DTranspose(512, (3, 3), activation="relu", padding="same")(x)
    x = BatchNormalization()(x)

    # ---------- block4

    x = UpSampling2D((2, 2))(x)
    x = Conv2DTranspose(512, (3, 3), activation="relu", padding="same")(x)
    x = BatchNormalization()(x)
    x = Conv2DTranspose(512, (3, 3), activation="relu", padding="same")(x)
    x = BatchNormalization()(x)
    x = Conv2DTranspose(512, (3, 3), activation="relu", padding="same")(x)
    x = BatchNormalization()(x)

    # ---------- block3

    x = UpSampling2D((2, 2))(x)
    x = Conv2DTranspose(256, (3, 3), activation="relu", padding="same")(x)
    x = BatchNormalization()(x)
    x = Conv2DTranspose(256, (3, 3), activation="relu", padding="same")(x)
    x = BatchNormalization()(x)
    x = Conv2DTranspose(256, (3, 3), activation="relu", padding="same")(x)
    x = BatchNormalization()(x)

    # ---------- block2

    x = UpSampling2D((2, 2))(x)
    x = Conv2DTranspose(128, (3, 3), activation="relu", padding="same")(x)
    x = BatchNormalization()(x)
    x = Conv2DTranspose(128, (3, 3), activation="relu", padding="same")(x)
    x = BatchNormalization()(x)

    # ---------- block1

    x = UpSampling2D((2, 2))(x)
    x = Conv2DTranspose(64, (3, 3), activation="relu", padding="same")(x)
    x = BatchNormalization()(x)
    x = Conv2DTranspose(64, (3, 3), activation="relu", padding="same")(x)
    x = BatchNormalization()(x)

    if class_or_regr == 0:
        final_filters = 3
    elif class_or_regr == 1:
        final_filters = 29

    decoder_output = Conv2DTranspose(
        final_filters, (3, 3), activation="softmax", padding="same"
    )(x)
    autoencoder = Model(encoder_input, decoder_output)

    return autoencoder


def ae_predict(
    model, im_path, im_gt_path, lower_bound, upper_bound, specification, class_or_regr
):

    for index, file_path in enumerate(glob.glob(im_path + "/*.png")):

        if index <= lower_bound or index > upper_bound:
            continue

        # Resize Image to network input size
        # Untouched image
        image = Image.open(file_path)
        image = image.resize((608, 176), Image.NEAREST)

        # Resize ground truth for visualization
        image_gt = Image.open(im_gt_path + "/" + os.path.basename(file_path))
        image_gt = image_gt.resize((608, 176), Image.NEAREST)

        image_array = np.asarray(image)

        image_array.astype("float32")
        image_array = image_array / 255

        image_array = np.expand_dims(image_array, axis=0)

        prediction = model.predict(image_array)

        if class_or_regr == 0:

            prediction = prediction * 255

            prediction = prediction.astype("uint8")
            prediction = np.squeeze(prediction, axis=0)

        elif class_or_regr == 1:
            prediction = get_prediction(prediction, rgb_array)

        plt.subplots(figsize=(15, 15))
        num_columns = 3
        num_rows = 1
        for i in range(0, 3):

            plt.subplot(num_rows, num_columns, i + 1)
            if i == 0:
                plt.imshow(image)
            if i == 1:
                plt.imshow(image_gt)
            if i == 2:
                plt.imshow(prediction)
                plt.imsave(
                    "logs/autoencoder_logs/"
                    + specification
                    + "/prediction"
                    + str(index)
                    + ".png",
                    prediction,
                )

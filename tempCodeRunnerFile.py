#To test for individual images

# mymodel=load_model('mymodel.h5')
# test_image=image.load_img(r'E:\placement Resume\FaceMaskDetector-master\FaceMaskDetector-master\mask.png',target_size=(150,150,3))
# # test_image=image.load_img('E:\placement Resume\FaceMaskDetector-master\FaceMaskDetector-master\temp.jpg',
# #                           target_size=(150,150,3))

# test_image=image.img_to_array(test_image)
# test_image=np.expand_dims(test_image,axis=0)
# mymodel.predict(test_image)[0][0]
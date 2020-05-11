def np_normalize(array):
    x_min = np.min(array)
    x_range = np.max(array) - np.min(array)  
    n = np.prod(array.shape[:-1])
    dim = array.shape
    return (array - x_min) / x_range

##

deformed_images = np_normalize(np.copy(ld_img_batch[no_orig:])[:,1:15,1:15,2:5])
deformed_labels = np_normalize(np.argmax(np.copy(ld_label_batch[no_orig:]), -1))

real_images = np_normalize(np.copy(ld_img_batch_tmp[no_orig:])[:,1:15,1:15,2:5])
real_labels = np_normalize(np.copy(ld_label_batch_tmp[no_orig:]))

##

import matplotlib.pyplot as plt

def highlight_cell(x,y, ax=None, **kwargs):
    rect = plt.Rectangle((x-.5, y-.5), 1,1, fill=False, **kwargs)
    ax = ax or plt.gca()
    ax.add_patch(rect)
    return rect

# Plot Images along chosen axes
def plot_deformed_imgs(deformed_images, deformed_labels, real_images, real_labels, plot_ax=(7,2)):
    
    assert len(deformed_images) == plot_ax[0], "dimensions do not match"
    
    plt.figure(figsize=(10,30))
    gs1 = gridspec.GridSpec(plot_ax[0], plot_ax[1])
    gs1.update(wspace=0.1, hspace=0.2) # set the spacing between axes. 
    
    i = 0 
    for n in range(plot_ax[0]):
        plt.subplot(gs1[i])
        plt.imshow(real_images[n])
        for x in range(real_labels[n].shape[0]):
            for y in range(real_labels[n].shape[1]):
                if(real_labels[n][y,x] == 1):
                    highlight_cell(x,y,color="red", linewidth=2)
        plt.title('True RGB Image')

        plt.subplot(gs1[i+1])
        plt.imshow(deformed_images[n])
        for x in range(deformed_labels[n].shape[0]):
            for y in range(deformed_labels[n].shape[1]):
                if(deformed_labels[n][y,x] == 1):
                    highlight_cell(x,y,color="red", linewidth=2)
        plt.title('Deformed RGB')
        i += 2
    plt.savefig("deformed.png", dpi=300)
    plt.show()

##

plot_deformed_imgs(deformed_images, deformed_labels, real_images, real_labels, plot_ax=(7,2))
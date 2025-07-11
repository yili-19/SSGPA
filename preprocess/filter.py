import json
import re
import os

def preprocess_caption(caption, max_words=32):
    caption = re.sub(
        r"([.!\"()*#:;~])",
        " ",
        caption.lower(),
    )
    caption = re.sub(
        r"\s{2,}",
        " ",
        caption,
    )
    caption = caption.rstrip("\n")
    caption = caption.strip(" ")

    # truncate caption
    caption_words = caption.split(" ")
    if len(caption_words) > max_words:
        caption = " ".join(caption_words[: max_words])

    return caption

DATA_PATH = {'spot':{
                    'train': r"/home/liyi/data/spot/captions/ori_train.json",
                    'val': r"/home/liyi/data/spot/captions/ori_val.json",
                    'test': r"/home/liyi/data/spot/captions/ori_test.json"
                    }
}
load_data_path = DATA_PATH['spot']['train']

invalid_captions = []
valid_captions = []

invalid_imgs = []
valid_imgs = []

data = json.load(open(load_data_path,'r'))

# filter captions
for i, item in enumerate(data):
    img_id = item['img_id']
    captions = item['sentences']

    filter_captions = []
    for cap in captions:
        cap = preprocess_caption(cap)
        if len(cap) < 4:
            continue
        filter_captions.append(cap)

    if len(filter_captions) == 0:
        if img_id not in invalid_imgs:
            invalid_imgs.append(img_id)
            invalid_captions.append({'img_id':img_id, 'sentences':captions})
        else:
            index = invalid_imgs.index(img_id)
            assert invalid_captions[index]['img_id'] == img_id, 'this item does not match the image id!(invalid)'
            invalid_captions[index]['sentences'].extend(captions)
    else:
        if img_id not in valid_imgs:
            valid_imgs.append(img_id)
            valid_captions.append({'img_id':img_id, 'sentences':filter_captions})
        else:
            index = valid_imgs.index(img_id)
            assert valid_captions[index]['img_id'] == img_id, 'this item does not match the image id!(valid)'
            valid_captions[index]['sentences'].extend(filter_captions)

vaild_save_path = os.path.join(os.path.dirname(load_data_path), 'filter_%s.json' % os.path.basename(load_data_path).split('.')[0])
invaild_save_path = os.path.join(os.path.dirname(load_data_path), 'invalid_%s.json' % os.path.basename(load_data_path).split('.')[0])

json.dump(valid_captions, open(vaild_save_path, 'w'))
json.dump(invalid_captions, open(invaild_save_path, 'w'))
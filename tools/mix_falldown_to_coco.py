import json
import os


"""
cd datasets
mkdir -p mix_det/annotations
cp mot/annotations/val_half.json mix_det/annotations/val_half.json
cp mot/annotations/test.json mix_det/annotations/test.json
cd mix_det
ln -s ../mot/train mot_train
ln -s ../crowdhuman/CrowdHuman_train crowdhuman_train
ln -s ../crowdhuman/CrowdHuman_val crowdhuman_val
ln -s ../Cityscapes cp_train
ln -s ../ETHZ ethz_train
cd ..
"""
img_list = list()
ann_list = list()

bytetrack_mix_data = json.load(open('/home/jhs/YOLOX/datasets/annotations/split_train.json', 'r'))
print('기존 mix_det 데이터셋의 이미지 수: ', len(bytetrack_mix_data['images']))
for img in bytetrack_mix_data['images']:
    img_list.append(img)

for ann in bytetrack_mix_data['annotations']:
    ann_list.append(ann)

# video_list = bytetrack_mix_data['videos']
video_list = [{"id": 1, "file_name": "MOT17-02-FRCNN"}, {"id": 2, "file_name": "MOT17-04-FRCNN"}, {"id": 3, "file_name": "MOT17-05-FRCNN"}, {"id": 4, "file_name": "MOT17-09-FRCNN"}, {"id": 5, "file_name": "MOT17-10-FRCNN"}, {"id": 6, "file_name": "MOT17-11-FRCNN"}, {"id": 7, "file_name": "MOT17-13-FRCNN"}, {"id": 10, "file_name": "crowdhuman_train"}, {"id": 10, "file_name": "crowdhuman_val"}, {"id": 10, "file_name": "ethz"}, {"id": 10, "file_name": "cityperson"}]
category_list = bytetrack_mix_data['categories']

merge_json = json.load(open('datasets/annotations/falldown_coco_updated2.json', 'r'))
print('falldownframes1 데이터셋의 이미지 수: ', len(merge_json['images']))
max_img = 100000
max_ann = 45000000      
max_video = 10

img_id_count = 0
for img in merge_json['images']:
    img_id_count += 1
    img['file_name'] = img['file_name']
    img['frame_id'] = img_id_count
    img['prev_image_id'] = img['id'] + max_img
    img['next_image_id'] = img['id'] + max_img
    img['id'] = img['id'] + max_img
    img['video_id'] = max_video
    img_list.append(img)

for ann in merge_json['annotations']:
    ann['id'] = ann['id'] + max_ann
    ann['image_id'] = ann['image_id'] + max_img
    ann['category_id'] = 1
    ann['track_id'] = -1
    ann['bbox_vis'] = ann['bbox']
    ann['area'] = ann['bbox'][2] * ann['bbox'][3]
    ann_list.append(ann)

video_list = {
    'id': max_video,
    'file_name': 'falldownframes1'
}

merge_json = json.load(open('datasets/train2017/falldown_merge_0112/merged.json', 'r'))
print('falldown_merge_0112 데이터셋의 이미지 수: ', len(merge_json['images']))
max_img = 130000
max_ann = 50000000

img_id_count = 0
for img in merge_json['images']:
    img_id_count += 1
    img['file_name'] = 'falldown_merge_0112/' + img['file_name']
    img['frame_id'] = img_id_count
    img['prev_image_id'] = img['id'] + max_img
    img['next_image_id'] = img['id'] + max_img
    img['id'] = img['id'] + max_img
    img['video_id'] = max_video
    img_list.append(img)

for ann in merge_json['annotations']:
    ann['id'] = ann['id'] + max_ann
    ann['image_id'] = ann['image_id'] + max_img
    ann['category_id'] = 1
    ann['track_id'] = -1
    ann['bbox_vis'] = ann['bbox']
    ann['area'] = ann['bbox'][2] * ann['bbox'][3]
    ann_list.append(ann)

video_list = {
    'id': max_video,
    'file_name': 'falldown_merge_0112'
}

mix_json = dict()
mix_json['images'] = img_list
mix_json['annotations'] = ann_list
mix_json['videos'] = video_list
mix_json['categories'] = category_list
json.dump(mix_json, open('datasets/annotations/merged_testset_roboflow_bytetrack.json', 'w'))

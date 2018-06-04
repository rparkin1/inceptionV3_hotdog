# inceptionV3_hotdog

This project re-train's Google's Inception V3 model to recognize if an image is a hot dog or not a hot dog.



## Retrain the Inception V3 model with hotdog data
ARCHITECTURE=inception_v3

`python -m hotdog.retrain --bottleneck_dir=tf_files/bottlenecks  --how_many_training_steps=500  --model_dir=tf_files/models/  --summaries_dir=tf_files/training_summaries/${ARCHITECTURE} --output_graph=tf_files/retrained_graph.pb --output_labels=tf_files/retrained_labels.txt --image_dir=images --architecture=${ARCHITECTURE}
`

## Score the model
`python -m hotdog.label_image   \
   --graph=tf_files/retrained_graph.pb \
   --input_height=299 --input_width=299  \
   --image=images/hot_dog/hotdog-1.jpg
`

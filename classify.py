import tensorflow as tf, sys
from readcategory import readcategory
from flask import  redirect, url_for
from randomimage import getImage
def classify(name):
	image_path = name
	readCategoryStruct=readcategory();
	result='''<tr>'''
	# Read in the image_data
	image_data = tf.gfile.FastGFile(image_path, 'rb').read()

	# Loads label file, strips off carriage return
	label_lines = [line.rstrip() for line 
		           in tf.gfile.GFile("tf_files/output_labels.txt")]

	# Unpersists graph from file
	with tf.gfile.FastGFile("tf_files/output_graph.pb", 'rb') as f:
	    graph_def = tf.GraphDef()
	    graph_def.ParseFromString(f.read())
	    _ = tf.import_graph_def(graph_def, name='')
	images=""
	with tf.Session() as sess:
	    # Feed the image_data as input to the graph and get first prediction
	    softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')
	    
	    predictions = sess.run(softmax_tensor, \
		     {'DecodeJpeg/contents:0': image_data})
	    
	    # Sort to show labels of first prediction in order of confidence
	    top_k = predictions[0].argsort()[-len(predictions[0]):][::-1]
	    resultNumber=0
	    #print readCategoryStruct
	    for node_id in top_k:
		human_string = label_lines[node_id]
		score = predictions[0][node_id]
		#print('%s (score = %.5f)' % (human_string, score))
		if(resultNumber==0):
			similar=human_string
			resultT= "<tr>"+  ('<td>%s- <mark>%s</mark> </td><td> (score = %.5f) </td>' % (human_string,readCategoryStruct[human_string], score)) +  '</tr>'

		else:
			resultT= "<tr>"+  ('<td>%s- %s </td><td> (score = %.5f) </td>' % (human_string,readCategoryStruct[human_string], score)) +  '</tr>'
		result=result+resultT
		resultNumber=resultNumber+1
		if (resultNumber==10):
			for x in range(0, 20):
				filename='UECFOOD100/' + similar +"/" + getImage(similar)
				images = images + '''<img <img style="width:100px;height:100px; margin-top: 10px;"  src="'''+ url_for('static', filename=filename) + '''" /> '''

			return result + '</tr></table><frameset cols="25%,50%,25%"><frame src="frame_a.htm">' + "<h1>similares </h1>" + images

	    return result + '</table><center>'

#classify('static/4.jpg')

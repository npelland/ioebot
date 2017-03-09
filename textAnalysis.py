from monkeylearn import MonkeyLearn

ml = MonkeyLearn('<<API Key>>')
text_list = ["This is a text to test your classifier", "This is some more text"]
module_id = 'cl_qkjxv9Ly'
res = ml.classifiers.classify(module_id, text_list, sandbox=True)
print (res.result)

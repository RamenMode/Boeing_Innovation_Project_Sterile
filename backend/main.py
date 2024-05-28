import sklearn
import sklearn.model_selection
import sklearn.svm
import tensorflow as tf
import tensorflow_hub as hub
import numpy as np
import tqdm
import os
import pandas as pd

from classifier import Classifier
from embedder import Embedder
from sort_data import get_df


class Mainframe():
    def __init__(self):
        datapath = "./../data/"
        dataset = get_df(datapath)
        self.sentence_embedder = Embedder()
        em_descrep_narrative = np.array(self.sentence_embedder.embed(dataset['descrep_narrative'])).tolist()
        self.cols = ["wuc", "wc_code", "updown_ind", "action_taken", "trans_code", "type_maf_code", "type_maint_code", "malfunction_code"]
        wuc_class = Classifier("wuc")
        wc_code_class = Classifier("wc_code")
        updown_ind_class = Classifier("updown_ind")
        action_taken_class = Classifier("action_taken")
        trans_code_class = Classifier("trans_code")
        type_maf_code_class = Classifier("type_maf_code")
        type_maint_code_class = Classifier("type_maint_code")
        malfunction_code_class = Classifier("malfunction_code")
        self.classifiers = [wuc_class, wc_code_class, updown_ind_class, action_taken_class, trans_code_class, type_maf_code_class, type_maint_code_class, malfunction_code_class]
        count = 0
        for (col, classifier) in zip(self.cols, self.classifiers):
            print(col)
            print(type(dataset[col].copy()))
            print(type(np.array(em_descrep_narrative)))
            classifier.split_data(np.array(em_descrep_narrative), dataset[col].copy())
            count += 1
            print(count)
            classifier.train()
            classifier.test()
        print('finished')

    def get_datalog(self, user_input):
        output = {}
        em_input = np.array(self.sentence_embedder.embed(user_input)).tolist()
        for (col, classifier) in zip(self.cols, self.classifiers):
            output[col] = classifier.predict(em_input)
        return output


if  __name__ == "__main__":
    mainframe = Mainframe()

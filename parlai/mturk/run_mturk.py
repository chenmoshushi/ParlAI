# Copyright (c) 2017-present, Facebook, Inc.
# All rights reserved.
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree. An additional grant
# of patent rights can be found in the PATENTS file in the same directory.
from parlai.core.params import ParlaiParser
from core import manage_hit

# QA data collection
task_module_name = 'parlai.mturk.tasks.qa_data_collection'
Agent = __import__(task_module_name+'.agents', fromlist=['']).QADataCollectionAgent

# Model evaluator
# task_module_name = 'parlai.mturk.tasks.model_evaluator'
# Agent = __import__(task_module_name+'.agents', fromlist=['']).ModelEvaluatorAgent


task_config = __import__(task_module_name+'.task_config', fromlist=['']).task_config

print("Creating HIT tasks for "+task_module_name+" ...")

argparser = ParlaiParser(False, False)
argparser.add_parlai_data_path()
argparser.add_mturk_log_path()

manage_hit.create_hits(
	opt=argparser.parse_args(),
	task_config=task_config,
	task_module_name=task_module_name,
	bot=Agent(opt=argparser.parse_args()), 
	num_hits=2, # Number of HITs you want to create for this task
	hit_reward=0.05, # In US dollars
	is_sandbox=True, # We suggest that you run it in MTurk sandbox mode to test first before moving to live site
	verbose=True
)
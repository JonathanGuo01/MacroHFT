# MacroHFT
This is the official implementation of the KDD 2024 "MacroHFT: Memory Augmented Context-aware Reinforcement Learning On High Frequency Trading".
https://arxiv.org/abs/2406.14537

To run the demo code:

You may first download the dataset from Google Drive:

https://drive.google.com/drive/folders/1AYHy-wUV0IwPoA7E1zvMRPL3wK0tPNiY?usp=drive_link

and put the folder under data folder.

## Step 1
Run scripts/decomposition.sh for data decomposition and labeling. 
替代命令：
nohup python -u -m preprocess.decomposition > output.log 2>&1 &

## Step 2
Run scripts/low_level.sh for low-level policy optimization. 
替代命令：
nohup python -u -m RL.agent.low_level --alpha 1 --clf 'slope' --dataset 'ETHUSDT' --device 'cuda' --label label_1 >./logs/low_level/ETHUSDT/slope_1.log 2>&1 &
nohup python -u -m RL.agent.low_level --alpha 4 --clf 'slope' --dataset 'ETHUSDT' --device 'cuda' --label label_2 >./logs/low_level/ETHUSDT/slope_2.log 2>&1 &
nohup python -u -m RL.agent.low_level --alpha 0 --clf 'slope' --dataset 'ETHUSDT' --device 'cuda' --label label_3 >./logs/low_level/ETHUSDT/slope_3.log 2>&1 &
nohup python -u -m RL.agent.low_level --alpha 4 --clf 'vol' --dataset 'ETHUSDT' --device 'cuda' --label label_1 >./logs/low_level/ETHUSDT/slope_1.log 2>&1 &
nohup python -u -m RL.agent.low_level --alpha 1 --clf 'vol' --dataset 'ETHUSDT' --device 'cuda' --label label_2 >./logs/low_level/ETHUSDT/slope_2.log 2>&1 &
nohup python -u -m RL.agent.low_level --alpha 1 --clf 'vol' --dataset 'ETHUSDT' --device 'cuda' --label label_3 >./logs/low_level/ETHUSDT/slope_3.log 2>&1 &

## Step 3
Run scripts/high_level.sh for meta-policy optimization. 

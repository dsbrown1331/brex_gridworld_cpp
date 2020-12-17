# Safe Imitation Learning via Fast Bayesian Reward Inference from Preferences

Daniel S. Brown, Russell Coleman, Ravi Srinivasan, Scott Niekum

<p align="center">
  <a href="https://arxiv.org/abs/2002.09089">View on ArXiv</a> |
  <a href="https://sites.google.com/view/bayesianrex/">Project Website</a>
</p>



This repository mainly contains the C++ code used to conduct the gridworld experiments reported in the paper "Safe Imitation Learning via Fast Bayesian Reward Inference from Preferences" published at ICML 2020. There is also a simple piece of starter code for running Bayesian REX MCMC in python, given feature counts and preferences, but this only gives the reward function distribution and doesn't perform any MDP optimization.

If you are interested in the Atari experiments reported in the Appendix, please see this repo [bayesianrex](https://github.com/dsbrown1331/bayesianrex).

If you find this repository is useful in your research, please cite the paper:
```
@InProceedings{brown2020safe,
  title = {Safe Imitation Learning via Fast Bayesian Reward Inference from Preferences},
  author = {Brown, Daniel S. and  Coleman, Russell and Srinivasan, Ravi and Niekum, Scott},
  booktitle = {Proceedings of the 37th International Conference on Machine Learning (ICML)},
  year = {2020}
}
```




Note that this code repository is designed to test the final performance of Bayesian REX and Bayesian IRL, but has not been optimized for memory management or speed. 


  
  ### Getting started
  - `git clone https://github.com/dsbrown1331/brex_gridworld_cpp.git`
  - `cd brex_gridworld_cpp`
  - `mkdir build`
  

## Python basic implementation of Bayesian REX
See `python/bayesianREX_basic.py` for an example of how to run Bayesian REX via python. The code is a trimmed down version of the Atari code and could be adapted to work with any MDP where you have preferences over demonstrations. This code requires numpy and PyTorch.

The remainder of this repo discusses the C++ version of Bayesian REX.
 
## B-REX vs BIRL Ranked Suboptimal vs. Optimal Demonstrations
In this experiment we give the best kind of demonstration to each algorithm: ranked demos to Bayesian REX and optimal demos to Bayesian IRL. Given the same number of demos we investigate how they perform.

- Build the experiment
```
make brex_gridworld_basic_exp_optsubopt 
```
- Run the experiment
```
./brex_gridworld_basic_exp_optsubopt
```

This will run the experiment using the code in `src/brex_gridWorldBasicExperimentOptSubopt.cpp` and write the results to `./data/brex_gridworld_optsubopt/`
  
  Experiment will take around 10+ minutes to run since it runs 100 replicates for each number of demonstrations. Experiment parameters can be set in `src/brex_gridWorldBasicExperimentOptSubopt.cpp`. 

  - Generate the data shown in Table 7 of the [Bayesian REX paper](https://arxiv.org/pdf/2002.09089.pdf)
  ```
  python scripts/evaluatePolicyLossOptSubopt.py
  ```

  | Num. Demos            | 2 demo | 5 demos | 10 demos | 20 demos | 30 demos |
| ------------------- |:-----:   | :----:   | :----:    | :----:        | :----:        |
| B-IRL | 0.044 | 0.033 | 0.020 | 0.009 | 0.006 |
| B-REX | 1.779 | 0.421 | 0.019 |0.006 | 0.006 |



## B-REX vs BIRL both with Ranked Suboptimal Demos
Now we compare the performance when both Bayesian REX and Bayesian IRL receive ranked suboptimal demos. In this case Bayesian IRL performance suffers since it is not designed to work with suboptimal demos or rankings.

- Build the experiment
```
make brex_gridworld_basic_exp_ranked 
```
- Run the experiment
```
./brex_gridworld_basic_exp_ranked
```

This will run the experiment using the code in `src/brex_gridWorldBasicExperimentRanked.cpp` and write the results to `./data/brex_gridworld_ranked/`
  
  Experiment will take 10+ minutes to run since it runs 100 replicates for each number of demonstrations. Experiment parameters can be set in `src/brex_gridWorldBasicExperimentRanked.cpp`. 

  - Generate the data shown in Table 8 of the [Bayesian REX paper](https://arxiv.org/pdf/2002.09089.pdf)
  ```
  python scripts/evaluatePolicyLossRanked.py
  ```

  | Num. Demos            | 2 demo | 5 demos | 10 demos | 20 demos | 30 demos |
| ------------------- |:-----:   | :----:   | :----:    | :----:        | :----:        |
| B-IRL | 3.512 | 3.319 | 2.791 | 3.078 | 3.158 |
| B-REX | 1.796 | 0.393 | 0.026 | 0.006 | 0.006 |



## B-REX vs [Critique BIRL](https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=8460854) both with Ranked Suboptimal Demos
In this experiment we attempt to even the playing field for Bayesian IRL and use a version proposed by Cui and Niekum, [Critique BIRL](https://ieeexplore.ieee.org/stamp/stamp.jsp?arnumber=8460854) which can learn from good and bad demonstrations. We use the top X% of demos as good and bottom X% as bad.

- Build the experiment
```
make brex_gridworld_basic_exp_goodbad
```
- Run the experiment
```
./brex_gridworld_basic_exp_goodbad
```

This will run the experiment using the code in `src/brex_gridWorldBasicExperimentGoodBad.cpp` and write the results to `./data/brex_gridworld_goodbad/`
  
  Experiment will take several minutes to run since it runs 100 replicates for each number of demonstrations. Experiment parameters can be set in `src/brex_gridWorldBasicExperimentGoodBad.cpp`. 

  - Generate the data shown in Table 9 of the [Bayesian REX paper](https://arxiv.org/pdf/2002.09089.pdf)
  ```
  python scripts/evaluatePolicyLossRankedGoodBad.py
  ```

  | Num. Demos            | 2 demo | 5 demos | 10 demos | 20 demos | 30 demos |
| ------------------- |:-----:   | :----:   | :----:    | :----:        | :----:        |
| B-IRL | 1.120 | 0.843 | 1.124 | 2.111 |
| B-REX | 0.006 | 0.006 | 0.006 | 0.006 |
 

## B-REX vs BIRL both with optimal demonstrations
Now we compare the performance when both Bayesian REX and Bayesian IRL receive optimaldemos. To provide a proof of concept for how Bayesian REX could work in this setting we automatically generate ranked demonstrations by running rollouts from a random policy and provide pairwise preferences that prefer the optimal demonstrations to random rollouts from the same states. Note that in practice using varying amounts of noise to create a smoother performance degredation is preferrable (e.g. [D-REX](https://arxiv.org/pdf/1907.03976.pdf)).

- Build the experiment
```
make brex_gridworld_basic_exp_optnoise
```
- Run the experiment
```
./brex_gridworld_basic_exp_optnoise
```

This will run the experiment using the code in `src/brex_gridWorldBasicExperimentRanked.cpp` and write the results to `./data/brex_gridworld_ranked/`
  
  Experiment will take 10+ minutes to run since it runs 100 replicates for each number of demonstrations. Experiment parameters can be set in `src/brex_gridWorldBasicExperimentRanked.cpp`. 

  - Generate the data shown in Table 8 of the [Bayesian REX paper](https://arxiv.org/pdf/2002.09089.pdf)
  ```
  python scripts/evaluatePolicyOptNoise.py
  ```

  | Num. Demos            | 2 demo | 5 demos | 10 demos | 20 demos | 30 demos |
| ------------------- |:-----:   | :----:   | :----:    | :----:        | :----:        |
| B-IRL | 0.045 | 0.034 | 0.018 | 0.009 | 0.006 |
| B-REX + random rollouts | 0.051 | 0.045 | 0.040 | 0.034 | 0.034 |


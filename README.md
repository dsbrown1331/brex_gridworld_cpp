# brex_gridworld_cpp
Implementation of Bayesian REX for gridworld experiments in ICML 2020 paper.


  
  #### Getting started
  - Make a build directory: `mkdir build`
  
 
## B-REX vs BIRL Ranked Suboptimal vs. Optimal Demonstrations

- Build the experiment
```
make brex_gridworld_basic_exp_optsubopt 
```
- Run the experiment
```
./brex_gridworld_basic_exp_optsubopt
```

This will run the experiment using the code in `src/brex_gridWorldBasicExperimentOptSubopt.cpp` and write the results to `./data/brex_gridworld_optsubopt/`
  
  - Experiment will take some time to run since it runs 100 replicates for each number of demonstrations. Experiment parameters can be set in `src/brex_gridWorldBasicExperimentOptSubopt.cpp`. 

  - Once experiment has finished run `python scripts/evaluatePolicyLossOptSubopt.py` to generate the data shown in Table 7 of the [Bayesian REX paper](https://arxiv.org/pdf/2002.09089.pdf)

  | Num. Demos            | 2 demo | 5 demos | 10 demos | 20 demos | 30 demos |
| ------------------- |:-----:   | :----:   | :----:    | :----:        | :----:        |
| B-IRL | 0.044 | 0.033 | 0.020 | 0.009 | 0.006 |
| B-REX | 1.779 | 0.421 | 0.019 |0.006 | 0.006 |

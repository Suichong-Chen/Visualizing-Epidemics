import networkx as nx
import ndlib.models.ModelConfig as mc
import ndlib.models.epidemics as ep
from ndlib.viz.mpl.DiffusionTrend import DiffusionTrend


# random graph generator
g = nx.erdos_renyi_graph(1000, 0.1)
# g = nx.watts_strogatz_graph(30, 3, 0.1)

"""
Below is the SIR model simulation
initial set of infected nodes = 1%
beta - infection prob = 1%
gamma - removal prob = 0.5%
"""
# Model selection
model_SIR = ep.SIRModel(g)

# Model Configuration
cfg_SIR = mc.Configuration()
cfg_SIR.add_model_parameter('beta', 0.01)
cfg_SIR.add_model_parameter('gamma', 0.005)
cfg_SIR.add_model_parameter("fraction_infected", 0.01)
model_SIR.set_initial_status(cfg_SIR)

# Simulation execution
iterations = model_SIR.iteration_bunch(100)
trends = model_SIR.build_trends(iterations)

# Visualization
viz = DiffusionTrend(model_SIR, trends)
viz.plot("diffusion_for_SIR.pdf")

#--------------------------------------------------------------------------

"""
Below is the SIS model simulation
initial set of infected nodes = 1%
beta - infection prob = 1%
lambda - recovery prob = 0.5%
"""
model_SIS = ep.SISModel(g)

# Model Configuration
cfg_SIS = mc.Configuration()
cfg_SIS.add_model_parameter('beta', 0.01)
cfg_SIS.add_model_parameter('lambda', 0.005)
cfg_SIS.add_model_parameter("fraction_infected", 0.01)
model_SIS.set_initial_status(cfg_SIS)

# Simulation execution
iterations = model_SIS.iteration_bunch(100)
trends = model_SIS.build_trends(iterations)

# Visualization
viz = DiffusionTrend(model_SIS, trends)
viz.plot("diffusion_for_SIS.pdf")

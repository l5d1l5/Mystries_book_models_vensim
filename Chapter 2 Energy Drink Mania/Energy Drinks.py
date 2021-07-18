"""
Python model 'Energy Drinks.py'
Translated using PySD
"""


from pysd.py_backend.functions import Integ, lookup
from pysd import cache

__pysd_version__ = "1.8.1"

__data = {"scope": None, "time": lambda: 0}

_subscript_dict = {}

_namespace = {
    "TIME": "time",
    "Time": "time",
    "Absorption per hour": "absorption_per_hour",
    "Absorption time": "absorption_time",
    "Cans per hour": "cans_per_hour",
    "Elimination per hour": "elimination_per_hour",
    "Elimination time": "elimination_time",
    "Intake per hour": "intake_per_hour",
    "Mg caffeine in body": "mg_caffeine_in_body",
    "Mg caffeine in stomach": "mg_caffeine_in_stomach",
    "Mg caffeine per can": "mg_caffeine_per_can",
    "FINAL TIME": "final_time",
    "INITIAL TIME": "initial_time",
    "SAVEPER": "saveper",
    "TIME STEP": "time_step",
}

##########################################################################
#                            CONTROL VARIABLES                           #
##########################################################################


def _init_outer_references(data):
    for key in data:
        __data[key] = data[key]


def time():
    return __data["time"]()


@cache.run
def final_time():
    """
    Real Name: FINAL TIME
    Original Eqn: 55
    Units: Hour
    Limits: (None, None)
    Type: constant
    Subs: None

    The final time for the simulation.
    """
    return 55


@cache.run
def initial_time():
    """
    Real Name: INITIAL TIME
    Original Eqn: 0
    Units: Hour
    Limits: (None, None)
    Type: constant
    Subs: None

    The initial time for the simulation.
    """
    return 0


@cache.step
def saveper():
    """
    Real Name: SAVEPER
    Original Eqn: TIME STEP
    Units: Hour
    Limits: (0.0, None)
    Type: component
    Subs: None

    The frequency with which output is stored.
    """
    return time_step()


@cache.run
def time_step():
    """
    Real Name: TIME STEP
    Original Eqn: 0.25
    Units: Hour
    Limits: (0.0, None)
    Type: constant
    Subs: None

    The time step for the simulation.
    """
    return 0.25


##########################################################################
#                             MODEL VARIABLES                            #
##########################################################################


@cache.step
def absorption_per_hour():
    """
    Real Name: Absorption per hour
    Original Eqn: Mg caffeine in stomach/Absorption time
    Units:
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return mg_caffeine_in_stomach() / absorption_time()


@cache.run
def absorption_time():
    """
    Real Name: Absorption time
    Original Eqn: 1
    Units:
    Limits: (None, None)
    Type: constant
    Subs: None


    """
    return 1


def cans_per_hour():
    """
    Real Name: Cans per hour
    Original Eqn: WITH LOOKUP ( Time, ([(0,0)-(55,2)],(0,0),(3,0),(4,1),(7,1),(8,0),(55,0) ))
    Units:
    Limits: (None, None)
    Type: lookup
    Subs: None


    """
    return lookup(time(), [0, 3, 4, 7, 8, 55], [0, 0, 1, 1, 0, 0])


@cache.step
def elimination_per_hour():
    """
    Real Name: Elimination per hour
    Original Eqn: Mg caffeine in body/Elimination time
    Units:
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return mg_caffeine_in_body() / elimination_time()


@cache.run
def elimination_time():
    """
    Real Name: Elimination time
    Original Eqn: 11
    Units:
    Limits: (None, None)
    Type: constant
    Subs: None


    """
    return 11


@cache.step
def intake_per_hour():
    """
    Real Name: Intake per hour
    Original Eqn: Cans per hour*Mg caffeine per can
    Units:
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return cans_per_hour() * mg_caffeine_per_can()


@cache.step
def mg_caffeine_in_body():
    """
    Real Name: Mg caffeine in body
    Original Eqn: INTEG ( Absorption per hour-Elimination per hour, 0)
    Units:
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return _integ_mg_caffeine_in_body()


@cache.step
def mg_caffeine_in_stomach():
    """
    Real Name: Mg caffeine in stomach
    Original Eqn: INTEG ( Intake per hour-Absorption per hour, 0)
    Units:
    Limits: (None, None)
    Type: component
    Subs: None


    """
    return _integ_mg_caffeine_in_stomach()


@cache.run
def mg_caffeine_per_can():
    """
    Real Name: Mg caffeine per can
    Original Eqn: 100
    Units:
    Limits: (None, None)
    Type: constant
    Subs: None


    """
    return 100


_integ_mg_caffeine_in_body = Integ(
    lambda: absorption_per_hour() - elimination_per_hour(),
    lambda: 0,
    "_integ_mg_caffeine_in_body",
)


_integ_mg_caffeine_in_stomach = Integ(
    lambda: intake_per_hour() - absorption_per_hour(),
    lambda: 0,
    "_integ_mg_caffeine_in_stomach",
)

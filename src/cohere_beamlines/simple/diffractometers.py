from typing import NamedTuple


class Diffractometer(NamedTuple):
    """
    Encapsulates the "simple" diffractometer. Based on aps_34idc.

    A bare data container of axis conventions; all geometry logic now lives in
    the Instrument class (see cohere_beamlines.common.instr).
    """
    sampleaxes = ('y+', 'z-', 'y+')  # in xrayutilities notation
    detectoraxes = ('y+', 'x-')
    incidentaxis = (0, 0, 1)
    sampleaxes_name = ('Theta', 'Chi', 'Phi')
    sampleaxes_mne = ('th', 'chi', 'phi')
    detectoraxes_name = ('Delta', 'Gamma')
    detectoraxes_mne = ('delta', 'gamma')
    detectordist_name = 'camdist'
    detectordist_mne = 'detdist'

"""Petra3_P10 InstrTab schema. See aps_34idc/instr_schema.py for the format reference.

Quirks:
  - Metadata comes from a .fio file located via data_dir + sample,
    so SPEC_DRIVERS includes 'sample'.
  - Spec keys 'del' and 'gam' are the fio mnemonics for delta and gamma
    (matches detectoraxes_mne in diffractometers.py).
  - diffractometer / detector choices are declared explicitly: the
    diffractometers.py module imports hdf5plugin (optional dep), so
    auto-introspection would fail on hosts without it.
"""

INSTR_FIELDS = {
    'general': [
        {
            'key': 'diffractometer', 'label': 'diffractometer',
            'type': 'choice', 'choices': ['P10sixc'],
            'description': 'Diffractometer model used for this experiment.',
        },
        {
            'key': 'data_dir', 'label': 'data directory', 'type': 'dir',
            'description': 'Directory containing the raw detector frames and metadata.',
        },
        {
            'key': 'sample', 'label': 'sample',
            'description': 'Sample identifier (used to locate the .fio metadata file).',
        },
        {
            'key': 'darkfield_filename', 'label': 'darkfield file', 'type': 'file',
            'description': 'Dark-field reference image (subtracted from frames).',
        },
        {
            'key': 'detector_module', 'label': 'detector module',
            'type': 'choice', 'choices': ['e4m', 'e2500'],
            'description': 'Detector module identifier.',
        },
    ],
    'spec': [
        {'key': 'energy', 'label': 'energy', 'unit': 'keV', 'type': 'float',
         'description': 'Incident beam energy. Values below 1000 are treated as keV, otherwise eV.'},
        {'key': 'del', 'label': 'delta', 'unit': 'deg', 'type': 'float',
         'description': 'Delta detector motor.'},
        {'key': 'gam', 'label': 'gamma', 'unit': 'deg', 'type': 'float',
         'description': 'Gamma detector motor.'},
        {'key': 'detdist', 'label': 'detector distance', 'unit': 'mm',
         'type': 'float',
         'description': 'Sample-to-detector distance.'},
        {'key': 'mu', 'label': 'mu', 'unit': 'deg', 'type': 'float'},
        {'key': 'om', 'label': 'om', 'unit': 'deg', 'type': 'float'},
        {'key': 'chi', 'label': 'chi', 'unit': 'deg', 'type': 'float'},
        {'key': 'phi', 'label': 'phi', 'unit': 'deg', 'type': 'float'},
        {'key': 'scanmot', 'label': 'scan motor', 'type': 'choice',
         'choices': ['mu', 'om', 'chi', 'phi'],
         'description': 'Motor that defines the scan steps. Pick a listed '
                        'motor or use (custom...) to type a different name.'},
        {'key': 'scanmot_del', 'label': 'scan motor step', 'unit': 'deg',
         'type': 'float',
         'description': 'Step size between scan frames.'},
        {'key': 'detector', 'label': 'detector',
         'type': 'choice', 'choices': ['e4m', 'e2500'],
         'description': 'Detector hardware used for this experiment.'},
    ],
}

SPEC_DRIVERS = ('data_dir', 'diffractometer', 'sample')

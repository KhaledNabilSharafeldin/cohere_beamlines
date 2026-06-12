import cohere_beamlines.simple.diffractometers as diff
import cohere_beamlines.simple.detectors as det
from cohere_beamlines.common.instr import Instrument


class Instrument_simple(Instrument):
    """
      This class encapsulates instruments: diffractometer and detector used for that experiment.

      Stub / reference beamline (based on aps_34idc). It has no metadata source,
      so parse_metadata returns an empty dict and all instrument parameters are
      taken from config_instr (filled in by hand). Geometry is provided by the
      common Instrument base class.
    """

    def __init__(self, det_obj, diff_obj, conf_params):
        """
        Constructor

        :param det_obj: detector object, can be None
        :param diff_obj: diffractometer object, can be None
        :param conf_params: dict of configuration maps
        """
        super(Instrument_simple, self).__init__(det_obj, diff_obj, conf_params)


    def convert_units(self, params):
        """
        Converts detectordist value from mm to m.
        """
        params[self.diff_obj.detectordist_mne] = params[self.diff_obj.detectordist_mne] / 1000.0  # convert to meters
        return params


    def parse_metadata(self, scan, **kwargs):
        """
        Stub beamline: no metadata source. Geometry parameters are taken from
        config_instr, so an empty dict is returned.
        """
        return {}


    def datainfo4scans(self):
        """
        Finds info (e.g. directories) that correspond to the configured scans.
        """
        if self.det_obj is None:
            print('detector object not created, check config parameters')
        return self.det_obj.datainfo4scans(self.scan_ranges)


def create_instr(configs, **kwargs):
    """
    Build factory for the Instrument_simple class.

    :param configs: dict
        the configuration maps (must contain 'config' and 'config_instr')

    Returns
    -------
    Instrument_simple object
    """
    diff_obj = diff.Diffractometer()
    instr_config_params = configs['config_instr']
    det_name = instr_config_params.get('detector', None)
    if det_name is None:
        raise ValueError('detector name not configured in config_instr')

    det_params = dict(instr_config_params)
    if 'config_prep' in configs:
        det_params.update(configs['config_prep'])
    det_obj = det.create_detector(det_name, det_params)

    instr = Instrument_simple(det_obj, diff_obj, configs)
    main_conf = configs['config']
    if 'scan' in main_conf:
        instr.scan_ranges = [[int(main_conf['scan']), int(main_conf['scan'])]]

    return instr

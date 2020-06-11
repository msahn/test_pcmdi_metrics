import cdms2 as cdms
import cdutil
import genutil
import MV2

class LandSeaMask:
    def __init__(self, data):
        self.mask = cdutil.generateLandSeaMask(data[0])
        self.d, self.mask2 = genutil.grower(data, self.mask)

    def land(self):
        d_mask = MV2.masked_where(self.mask2 == 0., self.d)
        return d_mask

    def ocean(self):
        d_mask = MV2.masked_where(self.mask2 == 1., self.d)
        return d_mask


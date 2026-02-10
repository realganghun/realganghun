class ElecProduct:
    volume = 0

    def VolumeControl(self,volume):
        print('현재 볼륨 : ', volume)

class ElecTv(ElecProduct):
    def VolumeControl(self, volume):
        print('Tv의 볼륨 : ',volume)

class ElecRadio(ElecProduct):
    def VolumeControl(self, volume):
        print('라디오의 볼륨 : ', volume)

# pro1 = ElecRadio()
# pro1.VolumeControl(30)

# pro2 = ElecTv()
# pro2.VolumeControl(20)

products = [ElecTv(), ElecRadio()]

for p in products:
    p.VolumeControl(30)
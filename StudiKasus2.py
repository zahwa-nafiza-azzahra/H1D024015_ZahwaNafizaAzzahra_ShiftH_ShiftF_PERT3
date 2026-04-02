import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
import matplotlib.pyplot as plt

informasi   = ctrl.Antecedent(np.arange(0, 101, 1), 'informasi')
persyaratan = ctrl.Antecedent(np.arange(0, 101, 1), 'persyaratan')
petugas     = ctrl.Antecedent(np.arange(0, 101, 1), 'petugas')
sarpras     = ctrl.Antecedent(np.arange(0, 101, 1), 'sarpras')
kepuasan    = ctrl.Consequent(np.arange(0, 401, 1), 'kepuasan')

for var in [informasi, persyaratan, petugas, sarpras]:
    var['tidak_memuaskan'] = fuzz.trapmf(var.universe, [0, 0, 60, 75])
    var['cukup_memuaskan'] = fuzz.trimf(var.universe,  [60, 75, 90])
    var['memuaskan']       = fuzz.trapmf(var.universe, [75, 90, 100, 100])

kepuasan['tidak_memuaskan']  = fuzz.trapmf(kepuasan.universe, [0, 0, 50, 100])
kepuasan['kurang_memuaskan'] = fuzz.trimf(kepuasan.universe,  [75, 125, 175])
kepuasan['cukup_memuaskan']  = fuzz.trimf(kepuasan.universe,  [150, 225, 300])
kepuasan['memuaskan']        = fuzz.trimf(kepuasan.universe,  [250, 300, 350])
kepuasan['sangat_memuaskan'] = fuzz.trapmf(kepuasan.universe, [325, 375, 400, 400])

# 81 Aturan Fuzzy (dari file 81_fuzzy_rules.xlsx)
rules = [
    # Rule 1
    ctrl.Rule(informasi['tidak_memuaskan'] & persyaratan['tidak_memuaskan'] & petugas['tidak_memuaskan'] & sarpras['tidak_memuaskan'], kepuasan['kurang_memuaskan']),
    # Rule 2
    ctrl.Rule(informasi['tidak_memuaskan'] & persyaratan['tidak_memuaskan'] & petugas['tidak_memuaskan'] & sarpras['cukup_memuaskan'], kepuasan['cukup_memuaskan']),
    # Rule 3
    ctrl.Rule(informasi['tidak_memuaskan'] & persyaratan['tidak_memuaskan'] & petugas['tidak_memuaskan'] & sarpras['memuaskan'], kepuasan['cukup_memuaskan']),
    # Rule 4
    ctrl.Rule(informasi['tidak_memuaskan'] & persyaratan['tidak_memuaskan'] & petugas['cukup_memuaskan'] & sarpras['tidak_memuaskan'], kepuasan['cukup_memuaskan']),
    # Rule 5
    ctrl.Rule(informasi['tidak_memuaskan'] & persyaratan['tidak_memuaskan'] & petugas['cukup_memuaskan'] & sarpras['cukup_memuaskan'], kepuasan['cukup_memuaskan']),
    # Rule 6
    ctrl.Rule(informasi['tidak_memuaskan'] & persyaratan['tidak_memuaskan'] & petugas['cukup_memuaskan'] & sarpras['memuaskan'], kepuasan['cukup_memuaskan']),
    # Rule 7
    ctrl.Rule(informasi['tidak_memuaskan'] & persyaratan['tidak_memuaskan'] & petugas['memuaskan'] & sarpras['tidak_memuaskan'], kepuasan['cukup_memuaskan']),
    # Rule 8
    ctrl.Rule(informasi['tidak_memuaskan'] & persyaratan['tidak_memuaskan'] & petugas['memuaskan'] & sarpras['cukup_memuaskan'], kepuasan['cukup_memuaskan']),
    # Rule 9
    ctrl.Rule(informasi['tidak_memuaskan'] & persyaratan['tidak_memuaskan'] & petugas['memuaskan'] & sarpras['memuaskan'], kepuasan['memuaskan']),
    # Rule 10
    ctrl.Rule(informasi['tidak_memuaskan'] & persyaratan['cukup_memuaskan'] & petugas['tidak_memuaskan'] & sarpras['tidak_memuaskan'], kepuasan['cukup_memuaskan']),
    # Rule 11
    ctrl.Rule(informasi['tidak_memuaskan'] & persyaratan['cukup_memuaskan'] & petugas['tidak_memuaskan'] & sarpras['cukup_memuaskan'], kepuasan['cukup_memuaskan']),
    # Rule 12
    ctrl.Rule(informasi['tidak_memuaskan'] & persyaratan['cukup_memuaskan'] & petugas['tidak_memuaskan'] & sarpras['memuaskan'], kepuasan['cukup_memuaskan']),
    # Rule 13
    ctrl.Rule(informasi['tidak_memuaskan'] & persyaratan['cukup_memuaskan'] & petugas['cukup_memuaskan'] & sarpras['tidak_memuaskan'], kepuasan['cukup_memuaskan']),
    # Rule 14
    ctrl.Rule(informasi['tidak_memuaskan'] & persyaratan['cukup_memuaskan'] & petugas['cukup_memuaskan'] & sarpras['cukup_memuaskan'], kepuasan['cukup_memuaskan']),
    # Rule 15
    ctrl.Rule(informasi['tidak_memuaskan'] & persyaratan['cukup_memuaskan'] & petugas['cukup_memuaskan'] & sarpras['memuaskan'], kepuasan['memuaskan']),
    # Rule 16
    ctrl.Rule(informasi['tidak_memuaskan'] & persyaratan['cukup_memuaskan'] & petugas['memuaskan'] & sarpras['tidak_memuaskan'], kepuasan['cukup_memuaskan']),
    # Rule 17
    ctrl.Rule(informasi['tidak_memuaskan'] & persyaratan['cukup_memuaskan'] & petugas['memuaskan'] & sarpras['cukup_memuaskan'], kepuasan['memuaskan']),
    # Rule 18
    ctrl.Rule(informasi['tidak_memuaskan'] & persyaratan['cukup_memuaskan'] & petugas['memuaskan'] & sarpras['memuaskan'], kepuasan['memuaskan']),
    # Rule 19
    ctrl.Rule(informasi['tidak_memuaskan'] & persyaratan['memuaskan'] & petugas['tidak_memuaskan'] & sarpras['tidak_memuaskan'], kepuasan['cukup_memuaskan']),
    # Rule 20
    ctrl.Rule(informasi['tidak_memuaskan'] & persyaratan['memuaskan'] & petugas['tidak_memuaskan'] & sarpras['cukup_memuaskan'], kepuasan['cukup_memuaskan']),
    # Rule 21
    ctrl.Rule(informasi['tidak_memuaskan'] & persyaratan['memuaskan'] & petugas['tidak_memuaskan'] & sarpras['memuaskan'], kepuasan['memuaskan']),
    # Rule 22
    ctrl.Rule(informasi['tidak_memuaskan'] & persyaratan['memuaskan'] & petugas['cukup_memuaskan'] & sarpras['tidak_memuaskan'], kepuasan['cukup_memuaskan']),
    # Rule 23
    ctrl.Rule(informasi['tidak_memuaskan'] & persyaratan['memuaskan'] & petugas['cukup_memuaskan'] & sarpras['cukup_memuaskan'], kepuasan['memuaskan']),
    # Rule 24
    ctrl.Rule(informasi['tidak_memuaskan'] & persyaratan['memuaskan'] & petugas['cukup_memuaskan'] & sarpras['memuaskan'], kepuasan['memuaskan']),
    # Rule 25
    ctrl.Rule(informasi['tidak_memuaskan'] & persyaratan['memuaskan'] & petugas['memuaskan'] & sarpras['tidak_memuaskan'], kepuasan['memuaskan']),
    # Rule 26
    ctrl.Rule(informasi['tidak_memuaskan'] & persyaratan['memuaskan'] & petugas['memuaskan'] & sarpras['cukup_memuaskan'], kepuasan['memuaskan']),
    # Rule 27
    ctrl.Rule(informasi['tidak_memuaskan'] & persyaratan['memuaskan'] & petugas['memuaskan'] & sarpras['memuaskan'], kepuasan['sangat_memuaskan']),
    # Rule 28
    ctrl.Rule(informasi['cukup_memuaskan'] & persyaratan['tidak_memuaskan'] & petugas['tidak_memuaskan'] & sarpras['tidak_memuaskan'], kepuasan['cukup_memuaskan']),
    # Rule 29
    ctrl.Rule(informasi['cukup_memuaskan'] & persyaratan['tidak_memuaskan'] & petugas['tidak_memuaskan'] & sarpras['cukup_memuaskan'], kepuasan['cukup_memuaskan']),
    # Rule 30
    ctrl.Rule(informasi['cukup_memuaskan'] & persyaratan['tidak_memuaskan'] & petugas['tidak_memuaskan'] & sarpras['memuaskan'], kepuasan['cukup_memuaskan']),
    # Rule 31
    ctrl.Rule(informasi['cukup_memuaskan'] & persyaratan['tidak_memuaskan'] & petugas['cukup_memuaskan'] & sarpras['tidak_memuaskan'], kepuasan['cukup_memuaskan']),
    # Rule 32
    ctrl.Rule(informasi['cukup_memuaskan'] & persyaratan['tidak_memuaskan'] & petugas['cukup_memuaskan'] & sarpras['cukup_memuaskan'], kepuasan['cukup_memuaskan']),
    # Rule 33
    ctrl.Rule(informasi['cukup_memuaskan'] & persyaratan['tidak_memuaskan'] & petugas['cukup_memuaskan'] & sarpras['memuaskan'], kepuasan['memuaskan']),
    # Rule 34
    ctrl.Rule(informasi['cukup_memuaskan'] & persyaratan['tidak_memuaskan'] & petugas['memuaskan'] & sarpras['tidak_memuaskan'], kepuasan['cukup_memuaskan']),
    # Rule 35
    ctrl.Rule(informasi['cukup_memuaskan'] & persyaratan['tidak_memuaskan'] & petugas['memuaskan'] & sarpras['cukup_memuaskan'], kepuasan['memuaskan']),
    # Rule 36
    ctrl.Rule(informasi['cukup_memuaskan'] & persyaratan['tidak_memuaskan'] & petugas['memuaskan'] & sarpras['memuaskan'], kepuasan['memuaskan']),
    # Rule 37
    ctrl.Rule(informasi['cukup_memuaskan'] & persyaratan['cukup_memuaskan'] & petugas['tidak_memuaskan'] & sarpras['tidak_memuaskan'], kepuasan['cukup_memuaskan']),
    # Rule 38
    ctrl.Rule(informasi['cukup_memuaskan'] & persyaratan['cukup_memuaskan'] & petugas['tidak_memuaskan'] & sarpras['cukup_memuaskan'], kepuasan['cukup_memuaskan']),
    # Rule 39
    ctrl.Rule(informasi['cukup_memuaskan'] & persyaratan['cukup_memuaskan'] & petugas['tidak_memuaskan'] & sarpras['memuaskan'], kepuasan['memuaskan']),
    # Rule 40
    ctrl.Rule(informasi['cukup_memuaskan'] & persyaratan['cukup_memuaskan'] & petugas['cukup_memuaskan'] & sarpras['tidak_memuaskan'], kepuasan['cukup_memuaskan']),
    # Rule 41
    ctrl.Rule(informasi['cukup_memuaskan'] & persyaratan['cukup_memuaskan'] & petugas['cukup_memuaskan'] & sarpras['cukup_memuaskan'], kepuasan['memuaskan']),
    # Rule 42
    ctrl.Rule(informasi['cukup_memuaskan'] & persyaratan['cukup_memuaskan'] & petugas['cukup_memuaskan'] & sarpras['memuaskan'], kepuasan['memuaskan']),
    # Rule 43
    ctrl.Rule(informasi['cukup_memuaskan'] & persyaratan['cukup_memuaskan'] & petugas['memuaskan'] & sarpras['tidak_memuaskan'], kepuasan['memuaskan']),
    # Rule 44
    ctrl.Rule(informasi['cukup_memuaskan'] & persyaratan['cukup_memuaskan'] & petugas['memuaskan'] & sarpras['cukup_memuaskan'], kepuasan['memuaskan']),
    # Rule 45
    ctrl.Rule(informasi['cukup_memuaskan'] & persyaratan['cukup_memuaskan'] & petugas['memuaskan'] & sarpras['memuaskan'], kepuasan['sangat_memuaskan']),
    # Rule 46
    ctrl.Rule(informasi['cukup_memuaskan'] & persyaratan['memuaskan'] & petugas['tidak_memuaskan'] & sarpras['tidak_memuaskan'], kepuasan['cukup_memuaskan']),
    # Rule 47
    ctrl.Rule(informasi['cukup_memuaskan'] & persyaratan['memuaskan'] & petugas['tidak_memuaskan'] & sarpras['cukup_memuaskan'], kepuasan['memuaskan']),
    # Rule 48
    ctrl.Rule(informasi['cukup_memuaskan'] & persyaratan['memuaskan'] & petugas['tidak_memuaskan'] & sarpras['memuaskan'], kepuasan['memuaskan']),
    # Rule 49
    ctrl.Rule(informasi['cukup_memuaskan'] & persyaratan['memuaskan'] & petugas['cukup_memuaskan'] & sarpras['tidak_memuaskan'], kepuasan['memuaskan']),
    # Rule 50
    ctrl.Rule(informasi['cukup_memuaskan'] & persyaratan['memuaskan'] & petugas['cukup_memuaskan'] & sarpras['cukup_memuaskan'], kepuasan['memuaskan']),
    # Rule 51
    ctrl.Rule(informasi['cukup_memuaskan'] & persyaratan['memuaskan'] & petugas['cukup_memuaskan'] & sarpras['memuaskan'], kepuasan['sangat_memuaskan']),
    # Rule 52
    ctrl.Rule(informasi['cukup_memuaskan'] & persyaratan['memuaskan'] & petugas['memuaskan'] & sarpras['tidak_memuaskan'], kepuasan['memuaskan']),
    # Rule 53
    ctrl.Rule(informasi['cukup_memuaskan'] & persyaratan['memuaskan'] & petugas['memuaskan'] & sarpras['cukup_memuaskan'], kepuasan['sangat_memuaskan']),
    # Rule 54
    ctrl.Rule(informasi['cukup_memuaskan'] & persyaratan['memuaskan'] & petugas['memuaskan'] & sarpras['memuaskan'], kepuasan['sangat_memuaskan']),
    # Rule 55
    ctrl.Rule(informasi['memuaskan'] & persyaratan['tidak_memuaskan'] & petugas['tidak_memuaskan'] & sarpras['tidak_memuaskan'], kepuasan['cukup_memuaskan']),
    # Rule 56
    ctrl.Rule(informasi['memuaskan'] & persyaratan['tidak_memuaskan'] & petugas['tidak_memuaskan'] & sarpras['cukup_memuaskan'], kepuasan['cukup_memuaskan']),
    # Rule 57
    ctrl.Rule(informasi['memuaskan'] & persyaratan['tidak_memuaskan'] & petugas['tidak_memuaskan'] & sarpras['memuaskan'], kepuasan['memuaskan']),
    # Rule 58
    ctrl.Rule(informasi['memuaskan'] & persyaratan['tidak_memuaskan'] & petugas['cukup_memuaskan'] & sarpras['tidak_memuaskan'], kepuasan['cukup_memuaskan']),
    # Rule 59
    ctrl.Rule(informasi['memuaskan'] & persyaratan['tidak_memuaskan'] & petugas['cukup_memuaskan'] & sarpras['cukup_memuaskan'], kepuasan['memuaskan']),
    # Rule 60
    ctrl.Rule(informasi['memuaskan'] & persyaratan['tidak_memuaskan'] & petugas['cukup_memuaskan'] & sarpras['memuaskan'], kepuasan['memuaskan']),
    # Rule 61
    ctrl.Rule(informasi['memuaskan'] & persyaratan['tidak_memuaskan'] & petugas['memuaskan'] & sarpras['tidak_memuaskan'], kepuasan['memuaskan']),
    # Rule 62
    ctrl.Rule(informasi['memuaskan'] & persyaratan['tidak_memuaskan'] & petugas['memuaskan'] & sarpras['cukup_memuaskan'], kepuasan['memuaskan']),
    # Rule 63
    ctrl.Rule(informasi['memuaskan'] & persyaratan['tidak_memuaskan'] & petugas['memuaskan'] & sarpras['memuaskan'], kepuasan['sangat_memuaskan']),
    # Rule 64
    ctrl.Rule(informasi['memuaskan'] & persyaratan['cukup_memuaskan'] & petugas['tidak_memuaskan'] & sarpras['tidak_memuaskan'], kepuasan['cukup_memuaskan']),
    # Rule 65
    ctrl.Rule(informasi['memuaskan'] & persyaratan['cukup_memuaskan'] & petugas['tidak_memuaskan'] & sarpras['cukup_memuaskan'], kepuasan['memuaskan']),
    # Rule 66
    ctrl.Rule(informasi['memuaskan'] & persyaratan['cukup_memuaskan'] & petugas['tidak_memuaskan'] & sarpras['memuaskan'], kepuasan['memuaskan']),
    # Rule 67
    ctrl.Rule(informasi['memuaskan'] & persyaratan['cukup_memuaskan'] & petugas['cukup_memuaskan'] & sarpras['tidak_memuaskan'], kepuasan['memuaskan']),
    # Rule 68
    ctrl.Rule(informasi['memuaskan'] & persyaratan['cukup_memuaskan'] & petugas['cukup_memuaskan'] & sarpras['cukup_memuaskan'], kepuasan['memuaskan']),
    # Rule 69
    ctrl.Rule(informasi['memuaskan'] & persyaratan['cukup_memuaskan'] & petugas['cukup_memuaskan'] & sarpras['memuaskan'], kepuasan['sangat_memuaskan']),
    # Rule 70
    ctrl.Rule(informasi['memuaskan'] & persyaratan['cukup_memuaskan'] & petugas['memuaskan'] & sarpras['tidak_memuaskan'], kepuasan['memuaskan']),
    # Rule 71
    ctrl.Rule(informasi['memuaskan'] & persyaratan['cukup_memuaskan'] & petugas['memuaskan'] & sarpras['cukup_memuaskan'], kepuasan['sangat_memuaskan']),
    # Rule 72
    ctrl.Rule(informasi['memuaskan'] & persyaratan['cukup_memuaskan'] & petugas['memuaskan'] & sarpras['memuaskan'], kepuasan['sangat_memuaskan']),
    # Rule 73
    ctrl.Rule(informasi['memuaskan'] & persyaratan['memuaskan'] & petugas['tidak_memuaskan'] & sarpras['tidak_memuaskan'], kepuasan['memuaskan']),
    # Rule 74
    ctrl.Rule(informasi['memuaskan'] & persyaratan['memuaskan'] & petugas['tidak_memuaskan'] & sarpras['cukup_memuaskan'], kepuasan['memuaskan']),
    # Rule 75
    ctrl.Rule(informasi['memuaskan'] & persyaratan['memuaskan'] & petugas['tidak_memuaskan'] & sarpras['memuaskan'], kepuasan['sangat_memuaskan']),
    # Rule 76
    ctrl.Rule(informasi['memuaskan'] & persyaratan['memuaskan'] & petugas['cukup_memuaskan'] & sarpras['tidak_memuaskan'], kepuasan['memuaskan']),
    # Rule 77
    ctrl.Rule(informasi['memuaskan'] & persyaratan['memuaskan'] & petugas['cukup_memuaskan'] & sarpras['cukup_memuaskan'], kepuasan['sangat_memuaskan']),
    # Rule 78
    ctrl.Rule(informasi['memuaskan'] & persyaratan['memuaskan'] & petugas['cukup_memuaskan'] & sarpras['memuaskan'], kepuasan['sangat_memuaskan']),
    # Rule 79
    ctrl.Rule(informasi['memuaskan'] & persyaratan['memuaskan'] & petugas['memuaskan'] & sarpras['tidak_memuaskan'], kepuasan['sangat_memuaskan']),
    # Rule 80
    ctrl.Rule(informasi['memuaskan'] & persyaratan['memuaskan'] & petugas['memuaskan'] & sarpras['cukup_memuaskan'], kepuasan['sangat_memuaskan']),
    # Rule 81
    ctrl.Rule(informasi['memuaskan'] & persyaratan['memuaskan'] & petugas['memuaskan'] & sarpras['memuaskan'], kepuasan['sangat_memuaskan']),
]

kepuasan_ctrl = ctrl.ControlSystem(rules)
kepuasan_sim  = ctrl.ControlSystemSimulation(kepuasan_ctrl)

kepuasan_sim.input['informasi']   = 80
kepuasan_sim.input['persyaratan'] = 60
kepuasan_sim.input['petugas']     = 50
kepuasan_sim.input['sarpras']     = 90

kepuasan_sim.compute()

print("--- Hasil Perhitungan Pelayanan Masyarakat ---")
print(f"Nilai Tingkat Kepuasan: {kepuasan_sim.output['kepuasan']:.2f}")

kepuasan.view(sim=kepuasan_sim)
plt.show()

class Solution:
    def minNumberOfHours(self, initialEnergy, initialExperience, energy, experience):
        hours = 0
        total_energy = sum(energy)
        if initialEnergy <= total_energy:
            add = total_energy - initialEnergy + 1
            hours += add
            initialEnergy += add

        for e, x in zip(energy, experience):
            if initialExperience <= x:
                add = x - initialExperience + 1
                hours += add
                initialExperience += add
            initialEnergy -= e
            initialExperience += x
        return hours
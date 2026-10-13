class Solution:
    def earliestFinishTime(self, landStartTime, landDuration,
                            waterStartTime, waterDuration):

        ans = float('inf')

        # Land -> Water
        for i in range(len(landStartTime)):
            land_end = landStartTime[i] + landDuration[i]

            for j in range(len(waterStartTime)):
                water_end = max(
                    land_end,
                    waterStartTime[j]
                ) + waterDuration[j]

                ans = min(ans, water_end)

        # Water -> Land
        for i in range(len(waterStartTime)):
            water_end = waterStartTime[i] + waterDuration[i]

            for j in range(len(landStartTime)):
                land_end = max(
                    water_end,
                    landStartTime[j]
                ) + landDuration[j]

                ans = min(ans, land_end)

        return ans
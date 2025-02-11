import gin
import random

gin.external_configurable(random.uniform)
gin.external_configurable(random.triangular)

@gin.configurable
def simulate(random_func, n_samples):
    return sum(random_func() for i in range(n_samples))

if __name__ == "__main__":
    gin.parse_config_file('/Users/vamsi_mbmax/Library/CloudStorage/OneDrive-Personal/01_vam_PROJECTS/LEARNING/proj_Productivity/dev_proj_Productivity/practise_prod_python_tools/dev/practise_scripts/gin_practise_config.gin')
    print(simulate())

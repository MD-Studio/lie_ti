cwlVersion: v1.0
class: Workflow
inputs:
  # Grompp minimization
  min_mdp_file:
    type: File
  min_gro_file:
    type: File
  min_top_file:
    type: File
  min_tpr_file:
    type: string
  # mdrun 
  openmp_threads:
    type: int
  name_min: string
    
outputs:
  # grompp minimization
  output_min_tpr:
    type: File
    outputSource: minimization_1/output_min_tpr
  # mdrun minimization
  output_min_gro:
    type: File
    outputSource: minimization_2/output_min_gro
    
steps:
  minimization_1:
    run: it_minimization_1.cwl
    in:
      min_mdp_file: min_mdp_file
      min_gro_file: min_gro_file
      min_top_file: min_top_file
      min_tpr_file: min_tpr_file      
    out: [minimization_1_out, minimization_1_err, output_min_tpr]
  minimization_2:
    run: it_minimization_2
    in:
      openmp_threads: openmp_threads
      name_min: name_min
    out: [minimization_2_out, minimization_2_err]

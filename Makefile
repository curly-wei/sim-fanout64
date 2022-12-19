pyutil_path = ./pyutil

cir_dir = ./cir
cir_files = \
	fanout48.cir 
	
tb_dir = ${cir_dir}/tb
tb_file_ad8655 = ${tb_dir}/tb_ad8655.cir
tb_file_ad8397 = ${tb_dir}/tb_ad8397.cir

sim_target_ad8655 = ad8655-vo.ssv
sim_target_ad8397 = ad8397-vo.ssv

vi_pulse_file_name = pulse-in.ssv

cir_deps = \
	$(foreach i,${cir_files},$(addprefix ${cir_dir}/,${i}))

.PHONY: clean

###############################
## Run Sim
###############################
default:
	$(error "please set the simlulation target, e.g. make opa192")

ad8655: sim_ad8655 plot_ad8655
ad8397: sim_ad8397 plot_ad8397

sim_ad8655: ${sim_target_ad8655}
${sim_target_ad8655}: ${cir_deps} ${tb_file_ad8655}
	ngspice ${tb_file_ad8655}

sim_ad8397: ${sim_target_ad8397}
${sim_target_ad8397}: ${cir_deps} ${tb_file_ad8397}
	ngspice ${tb_file_ad8397}

plot_ad8655:
	python3 ${pyutil_path}/plt-tran.py \
		-o ${sim_target_ad8655} \
		-i ${vi_pulse_file_name}
plot_ad8397:
	python3 ${pyutil_path}/plt-tran.py \
		-o ${sim_target_ad8397} \
		-i ${vi_pulse_file_name}

clean:
	rm -r *.ssv

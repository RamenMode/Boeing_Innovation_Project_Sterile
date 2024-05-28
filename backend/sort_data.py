import os
import pandas as pd

def get_df(datapath):
    frames = []

    old = ['maf_status_code', 'total_awm_hrs', 'total_awp_hrs', 'wc_code',
            'updown_ind', 'action_taken', 'trans_code', 'type_maf_code',
            'type_maint_code', 'malfunction_code', 'rmvd_partno',
            'rmvd_equip_serno', 'inst_partno', 'inst_equip_serno', 'corr_action',
            'descrep_narrative', 'system_reason_desc', 'id', 'Unnamed: 18',
            'Unnamed: 19', 'Unnamed: 20', 'Unnamed: 21', 'Unnamed: 22',
            'Unnamed: 23', 'Unnamed: 24', 'Unnamed: 25', 'Unnamed: 26',
            'Unnamed: 27', 'Unnamed: 28', 'Unnamed: 29', 'Unnamed: 30',
            'Unnamed: 31', 'Unnamed: 32', 'Unnamed: 33', 'Unnamed: 34',
            'Unnamed: 35', 'Unnamed: 36', 'Unnamed: 37']
    new = ['rcvd_date_time', 'buserno', 'wuc', 'emt', 'm3_hrs', 'm5_hrs', 'wp_hrs',
            'in_work_date_time', 'm4_hrs', 'comp_date_time',
            'last_altered_date_time', 'manhours', 'jcn', 'mcn', 'owner_org_code',
            'action_org_code', 'tec', 'assembly_code', 'data_source_name',
            'maint_level', 'maf_status_code', 'total_awm_hrs', 'total_awp_hrs',
            'wc_code', 'updown_ind', 'action_taken', 'trans_code', 'type_maf_code',
            'type_maint_code', 'malfunction_code', 'rmvd_partno',
            'rmvd_equip_serno', 'inst_partno', 'inst_equip_serno', 'corr_action',
            'descrep_narrative', 'system_reason_desc', 'id']
    df = pd.read_csv(f'{datapath}/Notre Dame Project Data - 1 of 10.csv')
    frames.append(df)
    for file in [f'{datapath}/Notre Dame Project Data - {i} of 10.csv' for i in range(2, 10)]:
        df = pd.read_csv(file)
        df = df.rename(columns=dict(zip(old, new)))
    df = pd.read_csv(f'{datapath}/Notre Dame Project Data - 10 of 10.csv')
    frames.append(df)
    dataset = pd.concat(frames)
    dataset.to_csv('output_filasde.csv', index=False)
    return dataset

if  __name__ == "__main__":
    get_df('./../data/')
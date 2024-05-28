import React from 'react';
import Button from '@mui/material/Button';
import TextField from '@mui/material/TextField';

export default function Page1({data}) {
    // Render page 1 with updated data
    return (
        <div>
            <h1>Categorize Maintenance</h1>
            <form className='form'>
                <div className='form-segment'>
                    <TextField required className='form-input' label="Action Taken" variant="filled" defaultValue={data.action_taken} />
                </div>
                <div className='form-segment'>
                    <TextField required className='form-input' label="Malfunction Code" variant="filled" defaultValue={data.malfunction_code} />
                </div>
                <div className='form-segment'>
                    <TextField required className='form-input' label="Trans Code" variant="filled" inputProps={{ type: 'number'}} defaultValue={data.trans_code} />
                </div>
                <div className='form-segment'>
                    <TextField required className='form-input' label="Type MAF Code" variant="filled"  defaultValue={data.type_maf_code} />
                </div>
                <div className='form-segment'>
                    <TextField required className='form-input' label="Type MAINT Code" variant="filled"  defaultValue={data.type_maint_code} />
                </div>
                <div className='form-segment'>
                    <TextField required className='form-input' label="Updown IND" variant="filled"  defaultValue={data.updown_ind} />
                </div>
                <div className='form-segment'>
                    <TextField required className='form-input' label="WC Code" variant="filled"  defaultValue={data.wc_code} />
                </div>
                <div className='form-segment'>
                    <TextField required className='form-input' label="WUC" variant="filled"  inputProps={{ type: 'number'}} defaultValue={data.wuc} />
                </div>

                <Button variant="contained" id='form-submit'>Submit</Button>
            </form>
        </div>
    )
}
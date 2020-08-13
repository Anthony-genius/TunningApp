import React from 'react';
import {Link} from 'react-router-dom';
import {Spacer} from '../Elements/Common';
import Brands from '../Components/Brands';
import {BackToOverviewButton} from '../Elements/Submit';
import {NewsItemPanel} from '../Elements/NewsPanel'
import Breadcrum from '../Components/Breadcrum'
import {connect} from 'react-redux'
import {NewsView} from '../Elements/Submission'

function SubmissionItemPage({submission_id, submissions}) {
  let data
  if (submissions && submissions.length > 0) {
    data = submissions.filter(item=>item.id===submission_id)[0]
  }
	const capitalize = (str, lower = false) =>
      (lower ? str.toLowerCase() : str).replace(/(?:^|\s|["'([{])+\S/g, match => match.toUpperCase());
    let text
    if (data) {
        text = capitalize(data.car_vin_number)
    }
return (
    <NewsItemPanel>
        <Breadcrum
                items={[
                  { url: "/submission", text: "Submissions" },
                  { url: `/submission/${submission_id}`, text: text },
                ]}
        />
        <Spacer />
        <NewsView>
        {
          data && (
            <div>
            <p><strong>Car VIN No: </strong>{data.car_vin_number}</p>
            <p><strong>Brand: </strong>{data.car_brand}</p>
            <p><strong>Build: </strong>{data.car_model}</p>
            <p><strong>Model: </strong>{data.car_build}</p>
            <p><strong>Engine Type: </strong>{data.engine_type}</p>
            <p><strong>Engine Power: </strong>{data.engine_power}</p>
            <p><strong>Year: </strong>{data.year}</p>
            <p><strong>Tuning Level: </strong>{data.tuning_level}</p>
            <p><strong>Reading Method: </strong>{data.reading_method}</p>
            <p><strong>ECU Type: </strong>{data.ecu_type}</p>
            <p><strong>Car Plate No: </strong>{data.car_plate_num}</p>
            <h3>The following files is uploaded</h3>
            {
              !data.file1 && !data.file2 && !data.file3 && !data.file4 && (<p>No files</p>)

            }
            <p>{data.file1}</p>
            <p>{data.file2}</p>
            <p>{data.file3}</p>
            <p>{data.file4}</p>
            </div>
            )
        }
            
        </NewsView>
        <Link to="/submission"><BackToOverviewButton value="BACK TO OVERVIEW" readOnly="true" /></Link>
        <Spacer />
        <Brands />
    </NewsItemPanel>
)
}
const mapStateToProps = (state, ownProps) => ({
  submission_id: ownProps.match.params.submission_id,
  submissions: state.blogs.submissions
})

export default connect(mapStateToProps, null)(SubmissionItemPage)


import React from 'react';
import Brands from '../Components/Brands';
import {Spacer} from '../Elements/Common';
import {DownloadableItem, Download} from '../Elements/DownloadPanel'
import {getDownloadSoftware} from '../store/action/actions'
import Breadcrum from '../Components/Breadcrum'
import {connect} from 'react-redux'
import {PageLoader} from '../Components/SpinnerLoader'
import {NewsPanel, SubmissionBlock, SubmissionTitle, SubmissionText, SubmissionLinkRM} from '../Elements/NewsPanel';


const DownloadSoftwarePage = ({getDownloadSoftware, download_softwares, history}) => {
    const [pageFlag, setPageFlag] = React.useState(false)
    React.useEffect(()=>{
        setPageFlag(true)
        getDownloadSoftware(setPageFlag)
    }, [])
    const handleClick = e => {
        const price = e.target.id
        const download_url = e.target.name
        history.push(`/payment?price=${price}&desc=Download Software&download_url=${download_url}`)
    }
    return(
        <NewsPanel>
            <Breadcrum
                items={[
                  { url: "/download-software", text: "Downloadable Softwares" },
                ]}
            />
            <Spacer />
            {
                pageFlag
                ? <PageLoader />
                : <span></span>
            }
            {
                download_softwares && download_softwares.length > 0 && download_softwares.map((item, index)=>(
                    <SubmissionBlock key={index}>
                                <SubmissionTitle>{item.name}</SubmissionTitle>
                                {
                                    item.price
                                    ? <SubmissionText>{item.price}$</SubmissionText>
                                    : <SubmissionText>Free</SubmissionText>
                                }

                                <SubmissionLinkRM id={item.price} name={item.downloadable_file} onClick={handleClick}>Pay for Download</SubmissionLinkRM>
                                <Download>
                                    <DownloadableItem id={item.name} href={item.downloadable_file} download>{item.name}</DownloadableItem>
                                </Download>
                    </SubmissionBlock>

                    
                ))
            }

            <Spacer />
            <Brands />
        </NewsPanel>

        )
}
const mapStateToProps = (state, ownProps) => ({
  download_softwares: state.blogs.download_softwares,
  history: ownProps.history,
})
const mapDispatchToProps = dispatch => ({
  getDownloadSoftware: getDownloadSoftware(dispatch),
})
export default connect(mapStateToProps, mapDispatchToProps)(DownloadSoftwarePage)
{/**/}
login='''
    mutation (
        $username: String!, 
        $password: String!, 
        $rememberme: Boolean, 
        $captchaValue: String, 
        $captchaKey: String,
        $captchaType: String
    ) {
        signinByUsername (
            username: $username, 
            password: $password, 
            rememberme: $rememberme, 
            captchaValue: $captchaValue, 
            captchaKey: $captchaKey,
            captchaType: $captchaType
        ) {
            
    id
    username
    nickname
    role
    isEmailAuth
    isSnsAuth
    isPhoneAuth
    studentTerm
    alarmDisabled
    status {
        userStatus
    }
    profileImage {
        
    id
    name
    label {
        
    ko
    en
    ja
    vn

    }
    filename
    imageType
    dimension {
        
    width
    height

    }
    trimmed {
        filename
        width
        height
    }

    }
    banned {
        username
        nickname
        reason
        bannedCount
        bannedType
        projectId
        startDate
        userReflect {
            status
            endDate
        }
    }
    isProfileBlocked

        }
    }'''
project='''
    mutation UPDATE_PROJECT(
        
    $id: ID!
    $name: String
    $speed: Int
    $objects: JSON
    $variables: JSON
    $messages: JSON
    $functions: JSON
    $tables: JSON
    $scenes: JSON
    $blockLog: JSON
    $interface: JSON
    $aiUtilizeBlocks: JSON
    $expansionBlocks: JSON
    $hardwareLiteBlocks: JSON
    $thumb: String
    $categoryCode: String
    $description: String
    $description2: String
    $description3: String
    $isopen: Boolean
    $isPracticalCourse: Boolean
    $group: ID
    $learning: String

    ) {
        updateProject(
            
    id: $id
    name: $name
    speed: $speed
    objects: $objects
    variables: $variables
    messages: $messages
    functions: $functions
    tables: $tables
    scenes: $scenes
    blockLog: $blockLog
    interface: $interface
    aiUtilizeBlocks: $aiUtilizeBlocks
    expansionBlocks: $expansionBlocks
    hardwareLiteBlocks: $hardwareLiteBlocks
    thumb: $thumb
    categoryCode: $categoryCode
    description: $description
    description2: $description2
    description3: $description3
    isopen: $isopen
    isPracticalCourse: $isPracticalCourse
    group: $group
    learning: $learning

        ) {
            
    status
    result

        }
    }
'''
loadStory='''
    query SELECT_ENTRYSTORY(
    $pageParam: PageParam
    $query: String
    $user: String
    $category: String
    $term: String
    $prefix: String
    $progress: String
    $discussType: String
    $searchType: String
    $searchAfter: JSON
){
        discussList(
    pageParam: $pageParam
    query: $query
    user: $user
    category: $category
    term: $term
    prefix: $prefix
    progress: $progress
    discussType: $discussType
    searchType: $searchType
    searchAfter: $searchAfter
) {
            total
            list {
                
	id
    content
    created
    commentsLength
    likesLength
    user {
        
    id
    nickname
    username
    profileImage {
        
    id
    name
    label {
        
    ko
    en
    ja
    vn

    }
    filename
    imageType
    dimension {
        
    width
    height

    }
    trimmed {
        filename
        width
        height
    }

    }
    status {
        following
        follower
    }
    description
    role

    }
    image {
        
    id
    name
    label {
        
    ko
    en
    ja
    vn

    }
    filename
    imageType
    dimension {
        
    width
    height

    }
    trimmed {
        filename
        width
        height
    }

    }
    sticker {
        
    id
    name
    label {
        
    ko
    en
    ja
    vn

    }
    filename
    imageType
    dimension {
        
    width
    height

    }
    trimmed {
        filename
        width
        height
    }

    }
    isLike

            }
            searchAfter
        }
    }'''
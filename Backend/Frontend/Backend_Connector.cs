


namespace Frontend
{
    
    public static class Backend_Connector
    {
        private static Backend.Service_Layer.Service_Controller sv;

        public static Backend.Service_Layer.Service_Controller get_service_controller()
        {
            if(sv==null)
            {
                sv = new Backend.Service_Layer.Service_Controller();
            }
            return sv; ;
        }

    }
}
